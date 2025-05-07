---
icon: diagram-project
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
```bash
bash -c 'n=10.10.10 ;for i in $(seq 1 254); do (timeout 2 ping -c 1 $n.$i | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}:" | tr -d ":" &); done; wait'
```
{% endcode %}
{% endtab %}

{% tab title="Nmap" %}
<pre class="language-bash" data-overflow="wrap"><code class="lang-bash"><strong>./nmap -sn 10.10.10.0/24
</strong></code></pre>
{% endtab %}

{% tab title="ARP" %}
```bash
arp -a
```
{% endtab %}
{% endtabs %}

## Port scan

{% tabs %}
{% tab title="Bash" %}
{% code overflow="wrap" %}
```bash
bash -c 'ip=<target>; for port in $(seq 1 65535); do bash -c "echo > /dev/tcp/$ip/$port" > /dev/null 2>&1 && echo -e "$port\033[K" & if [ $((port % 500)) -eq 0 ]; then wait; fi; echo -ne "$port/65535\r"; done; wait'
```
{% endcode %}
{% endtab %}

{% tab title="Nmap" %}
{% code overflow="wrap" %}
```bash
.\nmap -p- -sT -n -Pn -v --min-rate 10000 <target>
```
{% endcode %}
{% endtab %}

{% tab title="Proxychains" %}
### Proxychains -> Nmap

{% code overflow="wrap" %}
```bash
seq 1 65535 | xargs -P 500 -I {} proxychains -q nmap -sT -Pn -p{} -open --min-rate 5000 -n -vvv <target> 2>&1 | grep -Po '\d+(?=/tcp open)'
```
{% endcode %}

### Proxychains -> Bash

{% code overflow="wrap" %}
```bash
bash -c 'ip=<target>; for port in $(seq 1 65535); do proxychains -q bash -c "echo > /dev/tcp/$ip/$port" > /dev/null 2>&1 && echo -e "$port\033[K" & if [ $((port % 200)) -eq 0 ]; then wait; fi; echo -ne "$port/65535\r"; done; wait'
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Port forwarding

{% tabs %}
{% tab title="Chisel" %}
First, run the chisel server in reverse mode on your host:

```bash
chisel server -p 8081 --reverse
```

Then, connect the client to the server:

```bash
# Connect to chisel server on 10.10.10.10:8081
# Forward your 127.0.0.1:8080 to 10.10.10.20:80
chisel client 10.10.10.10:8081 R:8080:10.10.10.20:80

# Create proxy SOCKS5 on 127.0.0.1:1080
chisel client 10.10.10.10:8081 R:socks
```
{% endtab %}

{% tab title="Socat" %}
{% code overflow="wrap" %}
```bash
# Forward port 8080 to 10.10.10.20:80
socat tcp-l:8080,fork,reuseaddr tcp:10.10.10.20:80
```
{% endcode %}
{% endtab %}

{% tab title="SSH" %}
{% code overflow="wrap" %}
```bash
# Forward your 127.0.0.1:8080 to 10.10.10.20:80
ssh user@10.10.10.10 -L 8080:127.0.0.1:80

# Create proxy SOCKS5 on 127.0.0.1:1080
ssh user@10.10.10.10 -D 1080
```
{% endcode %}


{% endtab %}
{% endtabs %}

## Subnets

```sh
sshuttle -r '<user>:<password>@<target>' <subnet>/<cidr>
```
