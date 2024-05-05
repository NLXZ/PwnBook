# Reconnaissance

## Host Discovery

### ARP Scan

```bash
arp-scan -I <INTERFACE> --localnet --ignoredups
```

### Nmap Ping Scan

```bash
nmap -sn <NETWORK>/<MASK>
```

### Bash Ping Sweep

> Specify `<NETWORK>` without the last octet (e.g. `192.168.1`)

```bash
bash -c 'n=<NETWORK> ;for i in {1..254}; do \
(timeout 2 ping -c 1 $n.$i | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}:" | \
tr -d ":" &); done; wait'
```

## Port Scan

### Nmap TCP Port Scan

```bash
nmap -p- --open -sS -n -v -Pn --min-rate 5000 -oG allPorts <TARGET_IP>
```

### Bash TCP Port Scan

```bash
bash -c 'ip=<TARGET_IP>; for port in $(seq 1 65535); do \
(echo > /dev/tcp/$ip/$port) > /dev/null 2>&1 && \
echo -e "$port\033[K" & if [ $((port % 200)) -eq 0 ]; \
then wait; fi; echo -ne "$port/65535\r"; done; wait'
```

### Nmap UDP Port Scan

```bash
nmap -sU -F -oG udpPorts <TARGET_IP>
```

## Service Enumeration

### Services Info & Version

```bash
nmap -p<PORT/s> -sCV -oN portScan <TARGET_IP>
```
