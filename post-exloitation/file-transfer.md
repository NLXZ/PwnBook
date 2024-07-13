# File Transfer

{% hint style="info" %}
You can always check the integrity of the files by computing the md5 hash of the file to ensure it was transferred successfully:

```batch
# Linux
md5sum <file>

# Windows
certutil -hashfile <file> md5
```
{% endhint %}

## HTTP/PHP

### Python3

```bash
python3 -m http.server <port>
```

### Python2

```bash
python2 -m SimpleHTTPServer <port>
```

### PHP

```bash
php -S 0.0.0.0:<port>
```

### Download

#### Wget

```bash
wget <url>
```

#### Curl

```bash
curl -s <url> -o <output>
```

#### PowerShell

```powershell
(New-Object Net.WebClient).DownloadString('<url>') > <output>
```

#### Batch

```batch
certutil -urlcache -split -f <url> <output>
```

## SMB

### SMB Server

```bash
smbserver.py <share> $(pwd) -smb2support
```

### Download

#### Linux

```bash
smbclient //<ip>/<share> -c "get <file> <output>"
```

#### Windows

```powershell
# mount smb Share to drive
net use z: \\<ip>\share /user:<user> <pass>
# copy from share
copy \\<ip>\<share>\<file> <output>
```

## Ncat

### Send

```bash
nc -nlvp <port> < <file>
```

### Recieve

```bash
nc -nlvp <port> > <output>
```

## Bash

### Send

```bash
cat <file> > /dev/tcp/<ip>/<port>
```

### Recieve

```bash
cat < /dev/tcp/<target>/<port> > <output>
```
