# Reconnaissance

## Host Discovery

### ARP Scan

```bash
arp-scan -I <INTERFACE> --localnet --ignoredups
```

### Nmap Ping Scan

```bash
nmap -sn <NETWORK>/24
```

### Bash Ping Sweep

> Specify `<NETWORK>` without the last octet (e.g. `192.168.1`)

```bash
bash -c 'ip=<NETWORK> ;for i in $(seq 1 254); do \
timeout 1 bash -c "ping -c 1 $ip.$i" &>/dev/null && \
echo -e "$ip.$i\033[K" & done; wait'
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
nmap -p<PORTS> -sCV -oN portScan <TARGET_IP>
```

### Enumerate HTTP service

```bash
nmap -p<HTTP_PORTS> --script http-enum -oN webScan <TARGET_IP>
```

## Fuzzing and Brute-Force

### Gobuster

Files and directories

```bash
gobuster dir -u http://<TARGET>/ -w <WORDLIST>
```

Subdomains

```bash
gobuster vhost -u http://<TARGET>/ -w <WORDLIST>
```

Useful parameters: `--threads, -t` `--exclude-length` `--status-codes, -s` `--status-codes-blacklist, -b` `--no-tls-validation, -k` `--timeout`

### Wfuzz

Files and directories

```bash
wfuzz -w <WORDLIST> http://<TARGET>/FUZZ
```

Subdomains

```bash
wfuzz -w <WORDLIST> http://FUZZ.<TARGET>
```

### Hydra

> If the service is running on a non default port you can use: `-s <PORT>`

SSH Login

```bash
hydra -l <USER> -P <WORDLIST> <TARGET> ssh
```

HTTP Login

> On `<POST_DATA>` you can use this placeholders to use wordlists: `^USER^` and `^PASS^`

```bash
hydra -l <USER> -P <WORDLIST> <TARGET> http-post-form "<URL>:<POST_DATA>:<FAILED_LOGIN_STR>"
```
