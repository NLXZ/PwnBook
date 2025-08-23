---
icon: network-wired
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

# Network Services

## FTP

#### Anonymous login

{% code overflow="wrap" %}
```bash
ftp anonymous@<target>  # No password needed
```
{% endcode %}

#### Auto login

{% code overflow="wrap" %}
```bash
sshpass -p '<password>' ftp <user>@<target>
```
{% endcode %}

#### Browser URL

{% code overflow="wrap" %}
```bash
ftp://<user>:<password>@<target>
```
{% endcode %}

#### SSL

{% code overflow="wrap" %}
```bash
lftp <target> -e "set ssl:verify-certificate no; set ftp:ssl-force true"
```
{% endcode %}

#### Download all files

{% code overflow="wrap" %}
```bash
wget -r --user='<user>' --password='<password>' ftp://<target>
```
{% endcode %}

## SSH

#### Default credentials

Check for [default credentials](https://book.hacktricks.xyz/network-services-pentesting/pentesting-ssh#default-credentials) depending on the vendor:

<table data-header-hidden><thead><tr><th width="115"></th><th width="300"></th><th></th></tr></thead><tbody><tr><td><strong>Vendor</strong></td><td><strong>Usernames</strong></td><td><strong>Passwords</strong></td></tr><tr><td>APC</td><td>apc, device</td><td>apc</td></tr><tr><td>Brocade</td><td>admin</td><td>admin123, password, brocade, fibranne</td></tr><tr><td>Cisco</td><td>admin, cisco, enable, hsa, pix, pnadmin, ripeop, root, shelladmin</td><td>admin, Admin123, default, password, secur4u, cisco, Cisco, _Cisco, cisco123, C1sco!23, Cisco123, Cisco1234, TANDBERG, change_it, 12345, ipics, pnadmin, diamond, hsadb, c, cc, attack, blender, changeme</td></tr><tr><td>Citrix</td><td>root, nsroot, nsmaint, vdiadmin, kvm, cli, admin</td><td>C1trix321, nsroot, nsmaint, kaviza, kaviza123, freebsd, public, rootadmin, wanscaler</td></tr><tr><td>D-Link</td><td>admin, user</td><td>private, admin, user</td></tr><tr><td>Dell</td><td>root, user1, admin, vkernel, cli</td><td>calvin, 123456, password, vkernel, Stor@ge!, admin</td></tr><tr><td>EMC</td><td>admin, root, sysadmin</td><td>EMCPMAdm7n, Password#1, Password123#, sysadmin, changeme, emc</td></tr><tr><td>HP/3Com</td><td>admin, root, vcx, app, spvar, manage, hpsupport, opc_op</td><td>admin, password, hpinvent, iMC123, pvadmin, passw0rd, besgroup, vcx, nice, access, config, 3V@rpar, 3V#rpar, procurve, badg3r5, OpC_op, !manage, !admin</td></tr><tr><td>Huawei</td><td>admin, root</td><td>123456, admin, root, Admin123, Admin@storage, Huawei12#$, HwDec@01, hwosta2.0, HuaWei123, fsp200@HW, huawei123</td></tr><tr><td>IBM</td><td>USERID, admin, manager, mqm, db2inst1, db2fenc1, dausr1, db2admin, iadmin, system, device, ufmcli, customer</td><td>PASSW0RD, passw0rd, admin, password, Passw8rd, iadmin, apc, 123456, cust0mer</td></tr><tr><td>Juniper</td><td>netscreen</td><td>netscreen</td></tr><tr><td>NetApp</td><td>admin</td><td>netapp123</td></tr><tr><td>Oracle</td><td>root, oracle, oravis, applvis, ilom-admin, ilom-operator, nm2user</td><td>changeme, ilom-admin, ilom-operator, welcome1, oracle</td></tr><tr><td>VMware</td><td>vi-admin, root, hqadmin, vmware, admin</td><td>vmware, vmw@re, hqadmin, default</td></tr></tbody></table>

#### Auto login

```
sshpass -p '<password>' ssh <user>@<target>
```

#### Private key login

{% code overflow="wrap" %}
```bash
ssh -i id_rsa <user>@<target>
```
{% endcode %}

#### Generate RSA keys

{% code overflow="wrap" %}
```bash
ssh-keygen -t rsa -f id_rsa
```
{% endcode %}

## HTTP/HTTPS

#### Web Technologies

{% code overflow="wrap" %}
```bash
whatweb http://<target>
```
{% endcode %}

{% embed url="https://www.wappalyzer.com/apps/" %}
I also recommend using this browser extension.
{% endembed %}

#### File and Directory Enumeration

{% code overflow="wrap" %}
```bash
nmap -p80,443 --script http-enum <target>
```
{% endcode %}

{% code overflow="wrap" %}
```bash
gobuster dir -u http://<target>/ -w wordlist.txt
```
{% endcode %}

{% code overflow="wrap" %}
```bash
wfuzz -w wordlist.txt http://<target>/FUZZ
```
{% endcode %}

{% code overflow="wrap" %}
```bash
# Good option for BurpSuite requests
ffuf -request request.txt -w wordlist.txt http://<target>/
```
{% endcode %}

#### Subdomain Enumeration

{% code overflow="wrap" %}
```bash
gobuster vhost -u http://<target>/ -w wordlist.txt
```
{% endcode %}

{% code overflow="wrap" %}
```bash
wfuzz -H 'Host: FUZZ.<target>' -w wordlist.txt http://<target>/
```
{% endcode %}

#### User input

{% content-ref url="../web/vulnerabilites/" %}
[vulnerabilites](../web/vulnerabilites/)
{% endcontent-ref %}

## SMB

System enumeration with `enum4linux`

```bash
enum4linux -a [-u '<user>' -p '<password>'] <target>
```

#### Shares Enumeration

{% tabs %}
{% tab title="smbclient" %}
{% code overflow="wrap" %}
```bash
# null session
smbclient -N -L //<target>
# authenticated
smbclient -U '<user>[%<password>]' -L //<target>
# conect to a share
smbclient [-U '<user>[%<password>]'] //<target>/share
```
{% endcode %}
{% endtab %}

{% tab title="smbmap" %}
{% code overflow="wrap" %}
```bash
# null session
smbmap -H <target>
# authenticated
smbmap -u '<user>' -p '<password>' -H <target>
# recursive/non-recursive listing
smbmap [-u '<user>' -p '<password>'] -R/-r share -H <target>
```
{% endcode %}
{% endtab %}

{% tab title="netexec" %}
{% code overflow="wrap" %}
```bash
# null session
nxc smb <target> -u '' -p '' --shares
# authenticated
nxc smb <target> -u '<user>' -p '<password>' --shares
# List share
nxc smb <target> [-u '<user>' -p '<password>'] --share share
```
{% endcode %}
{% endtab %}

{% tab title="nmap" %}
{% code overflow="wrap" %}
```bash
nmap -p 139,445 --script "smb-enum-shares" <target>
```
{% endcode %}
{% endtab %}
{% endtabs %}

## RPC

#### Automated Enumeration

{% code overflow="wrap" %}
```bash
rpcdump.py <target>
```
{% endcode %}

#### Manual Enumeration

{% code overflow="wrap" %}
```bash
# null session
rpcclient -U '' -N <target>
# authenticated
rpcclient -U '<user>%<password>' -N <target>
# commands
rpcclient -U '[<user>%<password>]' -N <target> -c 'command'
```
{% endcode %}

