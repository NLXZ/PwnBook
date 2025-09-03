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

# Web Enumeration

## Web Technologies

{% code overflow="wrap" %}
```bash
whatweb <url> [-a <level>]
```
{% endcode %}

{% embed url="https://www.wappalyzer.com/apps/" %}
I also recommend using this browser extension.
{% endembed %}

## File and Directory Enumeration

{% code overflow="wrap" %}
```bash
nmap -p80,443 --script http-enum <target_ip>
```
{% endcode %}

{% code overflow="wrap" %}
```bash
gobuster dir -u <url> -w <wordlist>
```
{% endcode %}

{% code overflow="wrap" %}
```bash
wfuzz <url>/FUZZ -w <wordlist>
```
{% endcode %}

{% code overflow="wrap" %}
```bash
# Good option for BurpSuite requests
ffuf <url> -request request.txt -w <wordlist>
```
{% endcode %}

## Subdomain Enumeration

{% code overflow="wrap" %}
```bash
gobuster vhost -u <url> -w <wordlist>
```
{% endcode %}

{% code overflow="wrap" %}
```bash
wfuzz <url> -H 'Host: FUZZ.<domain>' -w <wordlist>
```
{% endcode %}
