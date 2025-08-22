---
icon: radar
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

# Reconnaissance

## Host discovery

{% tabs %}
{% tab title="ICMP" %}
{% code overflow="wrap" %}
```bash
nmap -sn 10.10.10.0/24
```
{% endcode %}
{% endtab %}

{% tab title="ARP" %}
{% code overflow="wrap" %}
```bash
arp-scan -I <interface> --localnet --ignoredups
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Port scanning

{% tabs %}
{% tab title="TCP SYN" %}
{% code overflow="wrap" fullWidth="false" %}
```bash
nmap -p- -sSCV -n -Pn --min-rate 10000 -T3 -v <target>
```
{% endcode %}
{% endtab %}

{% tab title="UDP" %}
{% code overflow="wrap" %}
```bash
nmap --top-ports 1000 -sU -n -Pn --min-rate 10000 <target>
```
{% endcode %}
{% endtab %}
{% endtabs %}

### Nmap scripts

{% code overflow="wrap" %}
```bash
nmap -p <ports> --script <script> <target>
```
{% endcode %}

<details>

<summary>Scripts usage</summary>

You can list all available Nmap scripts using the following commands:

{% code overflow="wrap" %}
```bash
 # List nmap nse scripts
 ls /usr/share/nmap/scripts | grep <service>
 # Get info about a script
 nmap --script-help <script>
```
{% endcode %}

</details>
