# File Transfer

{% hint style="info" %}
You can always check the integrity of the files using `md5sum` to ensure they were transferred successfully.
{% endhint %}

## Sending

### Python3

```bash
python3 -m http.server <PORT>
```

### Python2

```bash
python -m SimpleHTTPServer <PORT>
```

### PHP

```bash
php -S 0.0.0.0:<PORT>
```

### SMB

```bash
smbserver.py <SHARE_NAME> $(pwd) -smb2support
```

### Ncat

```bash
nc -nlvp <PORT> < <FILE>
```

### Bash

```bash
cat <FILE> > /dev/tcp/<IP>/<PORT>
```

## Receiving

### Ncat

```bash
nc -nlvp <PORT> > <OUTPUT_FILE>
```

### Bash

```bash
cat < /dev/tcp/<IP>/<PORT> > <OUTPUT_FILE>
```

### Wget

```bash
wget <URL>
```

### Curl

```bash
curl -s <URL> -o <OUTPUT_FILE>
```

### SMB

Linux

```bash
smbclient //<IP>/<SHARE_NAME> -c "get <FILE> <OUTPUT_FILE>"
```

Windows

```batch
copy \\<IP>\<SHARE_NAME>\<FILE> <OUTPUT_FILE>
```

### PowerShell

```powershell
(New-Object Net.WebClient).DownloadString('<URL>') > <OUTPUT_FILE>
```

### Batch

```batch
certutil -urlcache -split -f <URL> <OUTPUT_FILE>
```
