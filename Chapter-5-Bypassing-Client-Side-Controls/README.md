# Chapter 5 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

How can data be transmitted via the client in a way that prevents tampering attacks?

**ANSWER -**



---

## Question 2 -

An application developer wants to stop an attacker from performing brute-force attacks against the login function. Because the attacker may target multiple usernames, the developer decides to store the number of failed attempts in an encrypted cookie, blocking any request if the number of failed attempts exceeds five. How can this defense be bypassed?

**ANSWER -**



---

## Question 3 -

An application contains an administrative page that is subject to rigorous access controls. It contains links to diagnostic functions located on a different web server. Access to these functions should also be restricted to administrators only. Without implementing a second authentication mechanism, which of the following client-side mechanisms (if any) could be used to safely control access to the diagnostic functionality? Do you need any more information to help choose a solution?

1. The diagnostic functions could check the HTTP ```Referer``` header to confirm that the request originated on the main administrative page.

2. The diagnostic functions could validate the supplied cookies to confirm that these contain a valid session token for the main application.

3. The main application could set an authentication token in a hidden field that is included within the request. The diagnostic function could validate this to confirm that the user has a session on the main application.

**ANSWER -**



---

## Question 4 -

If a form field includes the attribute ```disabled=true```, it is not submitted with the rest of the form. How can you change this behavior?

**ANSWER -**



---

## Question 5 -

Are there any means by which an application can ensure that a piece of input validation logic has been run on the client?

**ANSWER -**

