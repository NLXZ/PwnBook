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

# File Upload

## Extensions

| PHP     | ASP         | Jsp     | Perl | ColdFusion | NodeJS |
| ------- | ----------- | ------- | ---- | ---------- | ------ |
| .php    | .asp        | .jsp    | .pl  | .cfm       | .js    |
| .php2   | .config     | .jspx   | .pm  | .cfml      | .json  |
| .php3   | .ashx       | .jsw    | .cgi | .cfc       | .node  |
| .php4   | .asmx       | .jsv    | .lib | .dbm       |        |
| .php5   | .aspq       | .jspf   |      |            |        |
| .php7   | .axd        | .wss    |      |            |        |
| .pht    | .cshtm      | .do     |      |            |        |
| .phpt   | .cshtml     | .action |      |            |        |
| .phtm   | .rem        |         |      |            |        |
| .phtml  | .soap       |         |      |            |        |
| .phps   | .vbhtm      |         |      |            |        |
| .phar   | .vbhtm      |         |      |            |        |
| .hphp   | .asa        |         |      |            |        |
| .module | .cer .shtml |         |      |            |        |
| .inc    | .shtml      |         |      |            |        |
| .ctp    |             |         |      |            |        |

## Filter Bypass

1. **Uppercase letters:** `.pHp, .pHP5, .PhAr`
2. **Double extension:**&#x20;
   * `.png.php`
   * `.gif.php`
3. **Null byte:**&#x20;
   * `.php%00.gif`
   * `.php\x00.gif`
4. **Special chars:**&#x20;
   * `file.php%20`
   * `file.php%0a`
   * `file.php%0d%0a`
   * `file.php/`
   * `file.php.\`
   * `file.php....`
5. **Content-Type:**&#x20;
   * `Content-Type : image/gif`
   * `Content-Type : image/png`
   * `Content-Type : image/jpeg`
6. **Magic numbers:**
   * GIF: `GIF8;`
   * PNG: `\x89PNG\r\n\x1a\n\0\0\0\rIHDR\0\0\x03H\0\xs0\x03[`
   * JPG: `\xff\xd8\xff`

## References

[https://book.hacktricks.xyz/pentesting-web/file-upload](https://book.hacktricks.xyz/pentesting-web/file-upload)

[https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files)
