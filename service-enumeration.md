# Service Enumeration

## HTTP/S

### Directory and File Enumeration

#### Nmap

```
nmap -p<HTTP_PORT/s> --script http-enum -oN webScan <TARGET_IP>
```

#### Gobuster

```bash
gobuster dir -u http://<TARGET>/ -w <WORDLIST>
```

> Useful parameters: `--threads, -t` `--exclude-length` `--status-codes, -s` `--status-codes-blacklist, -b` `--no-tls-validation, -k` `--timeout`

#### Wfuzz

```bash
wfuzz -w <WORDLIST> http://<TARGET>/FUZZ
```

> Useful parameters: `-t (threads)` `--hc/hl/hw/hh` `--sc/sl/sw/sh`

### Subdomain Enumeration

#### Gobuster

```bash
gobuster vhost -u http://<TARGET>/ -w <WORDLIST>
```

#### Wfuzz

```bash
wfuzz -w <WORDLIST> http://FUZZ.<TARGET>
```

