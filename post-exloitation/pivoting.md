# Pivoting

## Binaries

You can download some useful binaries such as chisel, socat, nmap, etc:\
[https://github.com/jpillora/chisel](https://github.com/jpillora/chisel)\
[https://github.com/3ndG4me/socat](https://github.com/3ndG4me/socat)\
[https://github.com/andrew-d/static-binaries](https://github.com/andrew-d/static-binaries/tree/master)

## Host discovery

### Nmap

```bash
nmap -sn 10.10.10.0/24
```

## Bash

```bash
bash -c 'n=<network> ;for i in {1..254}; do (timeout 2 ping -c 1 $n.$i | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}:" | tr -d ":" &); done; wait'
```

{% hint style="info" %}
Specify  the  `<network>` without the last octet `(e.g. 192.168.1)`
{% endhint %}

## Port scan

### Nmap TCP

```bash
nmap -p- --open -sT -n -v -Pn --min-rate 5000 -oN allPorts <target>
```

### Bash TCP

{% code overflow="wrap" %}
```bash
bash -c 'ip=<target>; for port in $(seq 1 65535); do bash -c "echo > /dev/tcp/$ip/$port" > /dev/null 2>&1 && echo -e "$port\033[K" & if [ $((port % 200)) -eq 0 ]; then wait; fi; echo -ne "$port/65535\r"; done; wait'
```
{% endcode %}

### Proxychains

#### Nmap

{% code overflow="wrap" %}
```bash
seq 1 65535 | xargs -P 500 -I {} proxychains -q nmap -sT -Pn -p{} -open --min-rate 5000 -n -vvv 10.10.10.10 2>&1 | grep -Po '\d+(?=/tcp open)'
```
{% endcode %}

#### Bash

{% code overflow="wrap" %}
```bash
bash -c 'ip=<target>; for port in $(seq 1 65535); do proxychains -q bash -c "echo > /dev/tcp/$ip/$port" > /dev/null 2>&1 && echo -e "$port\033[K" & if [ $((port % 200)) -eq 0 ]; then wait; fi; echo -ne "$port/65535\r"; done; wait'
```
{% endcode %}

## Port forwarding

### Chisel

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

### Socat

```bash
# Forward port 8080 to 10.10.10.20:80
socat tcp-l:8080,fork,reuseaddr tcp:10.10.10.20:80
```

### SSH

```bash
# Forward your 127.0.0.1:8080 to 10.10.10.20:80
ssh user@10.10.10.10 -L 8080:127.0.0.1:80

# Create proxy SOCKS5 on 127.0.0.1:1080
ssh user@10.10.10.10 -D 1080
```

