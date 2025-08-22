---
icon: arrow-right-arrow-left
---

# File Transfer

## Integrity verification

{% tabs %}
{% tab title="Linux" %}
{% code overflow="wrap" %}
```sh
md5sum <file>
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```sh
certutil -hashfile <file> md5
```
{% endcode %}
{% endtab %}
{% endtabs %}

## HTTP

### HTTP Server

{% tabs %}
{% tab title="Python3" %}
```sh
python3 -m http.server <port>
```
{% endtab %}

{% tab title="Python2" %}
```sh
python2 -m SimpleHTTPServer <port>
```
{% endtab %}

{% tab title="PHP" %}
```sh
php -S 0:<port>
```
{% endtab %}
{% endtabs %}

### Download

{% tabs %}
{% tab title="Wget" %}
{% code overflow="wrap" %}
```bash
wget <url>
```
{% endcode %}
{% endtab %}

{% tab title="Curl" %}
{% code overflow="wrap" %}
```bash
curl -s <url> -o <output>
```
{% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
(New-Object Net.WebClient).DownloadString('<url>') > <output>
```
{% endcode %}

{% code overflow="wrap" %}
```powershell
Invoke-WebRequest <url> -o <output>
```
{% endcode %}
{% endtab %}

{% tab title="CMD" %}
{% code overflow="wrap" %}
```sh
certutil -urlcache -split -f <url> <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## SMB

### SMB Server

```sh
smbserver.py <share> $(pwd) -smb2support [-username user -password pass]
```

### Download

{% tabs %}
{% tab title="Linux" %}
{% code overflow="wrap" %}
```sh
smbclient -U 'user[%pass]' //<ip>/<share> -c "get <file> <output>"
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```sh
# mount smb Share to drive
net use z: \\<ip>\<share> [/user:user pass]
# copy from share
copy \\<ip>\<share>\<file> <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Netcat

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```sh
nc -nlvp <port> < <file>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```sh
nc -nlvp <port> > <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Bash

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```sh
cat <file> > /dev/tcp/<ip>/<port>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```sh
cat < /dev/tcp/<target>/<port> > <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}
