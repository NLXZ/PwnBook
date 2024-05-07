# Reconnaissance

## Host Discovery

### ARP Scan

```bash
arp-scan -I <interface> --localnet --ignoredups
```

### Nmap Ping Scan

```bash
nmap -sn <network>/<mask>
```

### Bash Ping Sweep

```bash
bash -c 'n=<network> ;for i in {1..254}; do \
(timeout 2 ping -c 1 $n.$i | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}:" | \
tr -d ":" &); done; wait'
```

{% hint style="warning" %}
Specify  the `<network>`without the last octet`(e.g. 192.168.1)`
{% endhint %}

## Port Scan

### Nmap TCP Port Scan

```bash
nmap -p- --open -sS -n -v -Pn --min-rate 5000 -oG allPorts <target>
```

### Bash TCP Port Scan

```bash
bash -c 'ip=<target>; for port in $(seq 1 65535); do \
(echo > /dev/tcp/$ip/$port) > /dev/null 2>&1 && \
echo -e "$port\033[K" & if [ $((port % 200)) -eq 0 ]; \
then wait; fi; echo -ne "$port/65535\r"; done; wait'
```

### Nmap UDP Port Scan

```bash
nmap -sU -F -oG udpPorts <target>
```

### Service & Version Detection

```bash
nmap -p<port/s> -sCV -oN portScan <target>
```

### Nmap Scripts

```bash
nmap -p<port/s> --script <script> <target>
```

{% hint style="info" %}
You can list all available Nmap scripts using the following command:

```bash
 # List nmap nse scripts
 ls /usr/share/nmap/scripts | grep <service>
 # Get info about the script
 nmap --script-help <script>
```
{% endhint %}
