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
curl -s <url> -o <out_file>
```
{% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
(New-Object Net.WebClient).DownloadString('<url>') > <out_file>
```
{% endcode %}

{% code overflow="wrap" %}
```powershell
Invoke-WebRequest <url> -o <out_file>
```
{% endcode %}
{% endtab %}

{% tab title="CMD" %}
{% code overflow="wrap" %}
```sh
certutil -urlcache -split -f <url> <out_file>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## SMB

### SMB Server

```sh
smbserver.py <share_name> <share_path> -smb2support [-username <out_file> -password <out_file>]
```

### Download

{% tabs %}
{% tab title="Linux" %}
{% code overflow="wrap" %}
```sh
smbclient -U '<user>[%<password>]' //<ip>/<share> -c "get <src_file> <out_file>"
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```sh
# mount smb Share to drive
net use z: \\<ip>\<share> [/user:$USERNAME $PASSWORD]
# copy from share
copy \\<ip>\<share>\<src_file> <out_file>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Netcat

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```sh
nc -nlvp <port> < <src_file>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```sh
nc <ip> <port> > <out_file>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Bash

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```sh
cat <src_file> > /dev/tcp/<ip>/<port>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```sh
cat < /dev/tcp/<ip>/<port> > <out_file>
```
{% endcode %}
{% endtab %}
{% endtabs %}
