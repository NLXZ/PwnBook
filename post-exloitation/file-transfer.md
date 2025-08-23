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
md5sum $FILE
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```sh
certutil -hashfile $FILE md5
```
{% endcode %}
{% endtab %}
{% endtabs %}

## HTTP

### HTTP Server

{% tabs %}
{% tab title="Python3" %}
```sh
python3 -m http.server $PORT
```
{% endtab %}

{% tab title="Python2" %}
```sh
python2 -m SimpleHTTPServer $PORT
```
{% endtab %}

{% tab title="PHP" %}
```sh
php -S 0:$PORT
```
{% endtab %}
{% endtabs %}

### Download

{% tabs %}
{% tab title="Wget" %}
{% code overflow="wrap" %}
```bash
wget $URL
```
{% endcode %}
{% endtab %}

{% tab title="Curl" %}
{% code overflow="wrap" %}
```bash
curl -s $URL -o $OUTPUT_FILE
```
{% endcode %}
{% endtab %}

{% tab title="PowerShell" %}
{% code overflow="wrap" %}
```powershell
(New-Object Net.WebClient).DownloadString("$URL") > $OUTPUT_FILE
```
{% endcode %}

{% code overflow="wrap" %}
```powershell
Invoke-WebRequest $URL -o $OUTPUT_FILE
```
{% endcode %}
{% endtab %}

{% tab title="CMD" %}
{% code overflow="wrap" %}
```sh
certutil -urlcache -split -f $URL $OUTPUT_FILE
```
{% endcode %}
{% endtab %}
{% endtabs %}

## SMB

### SMB Server

```sh
smbserver.py $SHARE . -smb2support [-username $USERNAME -password $PASSWORD]
```

### Download

{% tabs %}
{% tab title="Linux" %}
{% code overflow="wrap" %}
```sh
smbclient -U 'user[%pass]' //$IP/$SHARE -c "get $FILE $OUTPUT_FILE"
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code overflow="wrap" %}
```sh
# mount smb Share to drive
net use z: \\$IP\$SHARE [/user:$USERNAME $PASSWORD]
# copy from share
copy \\$IP\$SHARE\$FILE $OUTPUT_FILE
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Netcat

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```sh
nc -nlvp $PORT < $OUTPUT_FILE
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```sh
nc -nlvp $PORT > $OUTPUT_FILE
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Bash

{% tabs %}
{% tab title="Send" %}
{% code overflow="wrap" %}
```sh
cat $FILE > /dev/tcp/$IP/$PORT>
```
{% endcode %}
{% endtab %}

{% tab title="Recieve" %}
{% code overflow="wrap" %}
```sh
cat < /dev/tcp/$IP/$PORT > $OUTPUT_FILE
```
{% endcode %}
{% endtab %}
{% endtabs %}
