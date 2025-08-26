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
for ip in <network_prefix>.{1..254}; do ((ping -c1 -W1 $ip &>/dev/null && echo $ip)&) done; wait
```
{% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
$t = 1..254 | % { [Net.NetworkInformation.Ping]::new().SendPingAsync("<network_prefix>.$_", 100) }; [Threading.Tasks.Task]::WaitAll($t); $t.Result.Where{$_.Status -eq "Success"}.Address.IPAddressToString
```
{% endcode %}
{% endtab %}

{% tab title="Nmap" %}
<pre class="language-sh" data-overflow="wrap"><code class="lang-sh"><strong>./nmap -sn &#x3C;subnet>
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
for port in {1..65535}; do ((bash -c "echo > /dev/tcp/<target_ip>/$port" 2>/dev/null && echo $port)&); (( port % 200 == 0 )) && wait; done; wait
```
{% endcode %}

> With progress:
>
> {% code overflow="wrap" %}
> ```sh
> for port in {1..65535}; do ((bash -c "echo > /dev/tcp/<target_ip>/$port" 2>/dev/null && echo -e "$port\033[K")&); (( port % 200 == 0 )) && wait && echo -ne "$port/65535\r"; done; wait
> ```
> {% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
$ip = "<target_ip>"; $pool = [RunspaceFactory]::CreateRunspacePool(1, 100); $pool.Open(); $rs = for ($p = 1; $p -le 1024; $p++) { $ps = [PowerShell]::Create(); $ps.RunspacePool = $pool; [void]$ps.AddScript({ param($ip, $p)try { $tcp = New-Object Net.Sockets.TcpClient; $r = $tcp.BeginConnect($ip, $p, $null, $null); if ($r.AsyncWaitHandle.WaitOne(300, $false) -and $tcp.Connected) { $tcp.EndConnect($r); $p } }finally { $tcp.Close() } }).AddArgument($ip).AddArgument($p); [PSCustomObject]@{P = $ps; S = $ps.BeginInvoke() } }; $rs | % { $r = $_.P.EndInvoke($_.S); if ($r) { $r }; $_.P.Dispose() }; $pool.Dispose()
```
{% endcode %}
{% endtab %}

{% tab title="Nmap" %}
{% code overflow="wrap" %}
```sh
./nmap -p- -sS -n -Pn --min-rate 10000 -v <target_ip>
```
{% endcode %}
{% endtab %}

{% tab title="Proxychains" %}
### Proxychains -> Nmap

{% code overflow="wrap" %}
```sh
for port in {1..65535}; do ((proxychains -q nmap -p$port -sT -n -Pn --open -v <target_ip> |& grep -Po '\d+(?=/tcp open)')&); (( port % 200 == 0 )) && wait; done; wait
```
{% endcode %}

### Proxychains -> Bash

{% code overflow="wrap" %}
```sh
for port in {1..65535}; do ((proxychains -q bash -c "echo > /dev/tcp/<target_ip>/$port" 2>/dev/null && echo $port)&); (( port % 100 == 0 )) && wait; done; wait
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Port forwarding

{% tabs %}
{% tab title="Chisel" %}
First, run the chisel server in reverse mode in your host:

{% code overflow="wrap" %}
```sh
chisel server -p <listener_port> --reverse
```
{% endcode %}

Then, connect to the server:

{% code overflow="wrap" %}
```sh
chisel client <listener_ip>:<listener_port> R:<local_port>:<remote_host>:<remote_port>
```
{% endcode %}

{% code overflow="wrap" %}
```sh
chisel client <listener_ip>:<listener_port> R:socks
```
{% endcode %}
{% endtab %}

{% tab title="Socat" %}
{% code overflow="wrap" %}
```sh
socat tcp-l:<local_port>,fork,reuseaddr tcp:<remote_host>:<remote_port>
```
{% endcode %}
{% endtab %}

{% tab title="SSH" %}
{% code overflow="wrap" %}
```sh
ssh <user>@<target_ip> -L <local_port>:<remote_host>:<remote_port>
```
{% endcode %}

{% code overflow="wrap" %}
```sh
ssh <user>@<target_ip> -D <socks_port>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Subnet forwarding

```sh
sshuttle -r <user>:<password>@<target_ip> <subnet>
```
