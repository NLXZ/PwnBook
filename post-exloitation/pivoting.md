---
layout:
  width: wide
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: false
---

# Pivoting

## Binaries

You can download some useful binaries such as chisel, socat, nmap, etc:\
[https://github.com/jpillora/chisel](https://github.com/jpillora/chisel)\
[https://github.com/3ndG4me/socat](https://github.com/3ndG4me/socat)\
[https://github.com/andrew-d/static-binaries](https://github.com/andrew-d/static-binaries/tree/master)

## Host discovery

{% tabs %}
{% tab title="Bash" %}
{% code overflow="wrap" %}
```sh
for ip in 10.10.10.{1..254}; do ((ping -c1 -W1 $ip &>/dev/null && echo $ip)&) done; wait
```
{% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
$t = 1..254 | % { [Net.NetworkInformation.Ping]::new().SendPingAsync("10.10.10.$_", 100) }; [Threading.Tasks.Task]::WaitAll($t); $t.Result.Where{$_.Status -eq "Success"}.Address.IPAddressToString
```
{% endcode %}
{% endtab %}

{% tab title="Nmap" %}
<pre class="language-sh" data-overflow="wrap"><code class="lang-sh"><strong>./nmap -sn 10.10.10.0/24
</strong></code></pre>
{% endtab %}

{% tab title="ARP" %}
```sh
arp -a
```
{% endtab %}
{% endtabs %}

## Port discovery

{% tabs %}
{% tab title="Bash" %}
{% code overflow="wrap" %}
```sh
for port in {1..65535}; do ((timeout 0.01 bash -c "echo > /dev/tcp/10.10.10.10/$port" 2>/dev/null && echo -e "$port\033[K")&); (( port % 500 == 0 )) && wait && echo -ne "$port/65535\r"; done; wait
```
{% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
$t = 1..10000 | % { $c = [System.Net.Sockets.TcpClient]::new(); [PSCustomObject]@{Port=$_; Task=$c.ConnectAsync($ip, $_); Client=$c }}; $null = [Threading.Tasks.Task]::WaitAll($t.Task, 100); $t | ? {$_.Task.IsCompleted -and $_.Client.Connected} | % {$_.Port; $_.Client.Dispose()}
```
{% endcode %}
{% endtab %}

{% tab title="Nmap" %}
{% code overflow="wrap" %}
```sh
.\nmap -p- -sT -n -Pn -v --min-rate 10000 <target>
```
{% endcode %}
{% endtab %}

{% tab title="Proxychains" %}
### Proxychains -> Nmap

{% code overflow="wrap" %}
```sh
seq 1 65535 | xargs -P 500 -I {} proxychains -q nmap -sT -Pn -p{} -open --min-rate 5000 -n -vvv <target> 2>&1 | grep -Po '\d+(?=/tcp open)'
```
{% endcode %}

### Proxychains -> Bash

{% code overflow="wrap" %}
```sh
bash -c 'ip=<target>; for port in $(seq 1 65535); do proxychains -q bash -c "echo > /dev/tcp/$ip/$port" > /dev/null 2>&1 && echo -e "$port\033[K" & if [ $((port % 200)) -eq 0 ]; then wait; fi; echo -ne "$port/65535\r"; done; wait'
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Port forwarding

{% tabs %}
{% tab title="Chisel" %}
First, run the chisel server in reverse mode on your host:

```sh
chisel server -p 8081 --reverse
```

Then, connect to the server:

```sh
# Forward port 8080 to 10.10.10.20:80
chisel client 10.10.10.10:8081 R:3306:127.0.0.1:3306

# Create proxy SOCKS5 on 127.0.0.1:1080
chisel client 10.10.10.10:8081 R:socks
```
{% endtab %}

{% tab title="Socat" %}
{% code overflow="wrap" %}
```sh
# Forward port 8080 to 10.10.10.20:80
socat tcp-l:8080,fork,reuseaddr tcp:10.10.10.20:80
```
{% endcode %}
{% endtab %}

{% tab title="SSH" %}
{% code overflow="wrap" %}
```sh
# Forward port 8080 to 127.0.0.1:80
ssh user@10.10.10.10 -L 8080:127.0.0.1:80

# Create proxy SOCKS5 on 127.0.0.1:1080
ssh user@10.10.10.10 -D 1080
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Subnet forwarding

```sh
sshuttle -r '<user>:<password>@<target>' <subnet>/<cidr>
```
