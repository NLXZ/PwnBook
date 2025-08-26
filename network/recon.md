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

# Network Reconnaissance

## Host discovery

{% tabs %}
{% tab title="ICMP" %}
{% code overflow="wrap" %}
```shell
nmap -sn <subnet>
```
{% endcode %}
{% endtab %}

{% tab title="ARP" %}
{% code overflow="wrap" %}
```shell
arp-scan -I <interface> --localnet --ignoredups
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Port scanning

{% tabs %}
{% tab title="TCP SYN" %}
{% code overflow="wrap" fullWidth="false" %}
```sh
nmap -p- -sSCV -n -Pn --min-rate 10000 -v <target_ip>
```
{% endcode %}
{% endtab %}

{% tab title="UDP" %}
{% code overflow="wrap" %}
```sh
nmap --top-ports 1000 -sU -n -Pn --min-rate 10000 <target_ip>
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Nmap scripts" %}
{% code overflow="wrap" %}
```sh
nmap -p $PORTS --script <script> <target_ip>
```
{% endcode %}

> You can list all available Nmap scripts using the following commands:
>
> {% code overflow="wrap" %}
> ```sh
> # List nmap nse scripts
> ls /usr/share/nmap/scripts | grep <service>
> # Get info about a script
> nmap --script-help <script>
> ```
> {% endcode %}
{% endtab %}
{% endtabs %}
