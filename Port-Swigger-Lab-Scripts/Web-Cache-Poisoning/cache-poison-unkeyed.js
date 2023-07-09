// The steps below are meant to solve the following lab:
// https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header

// The webpage accepts the following unkeyed header:
// X-Forwarded-Host

// Adding "X-Forwarded-Host: example.com" to our request headers and looking at the respone you'll find the following:
// <script type="text/javascript" src="//example.com/resources/js/tracking.js">

// Changing the X-Forwarded-Host headers value to [SUB_DOMAIN].exploit-server.net and,
// Changing the exploit server path to "/resources/js/tracking.js" and adding the following JavaScript to the file will alert the victims cookie:

alert(document.cookie)
