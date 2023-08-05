# Chapter 13 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

You discover an application function where the contents of a query string parameter are inserted into the ```Location``` header in an HTTP redirect. What three different types of attacks can this behavior potentially be exploited to perform?

**ANSWER -**

1. Cookie injection by ending the query string parameter's value with the new line and line feed characters followed by a new cookie.

2. Proxy server cache poisoning.

3. Redirection to a domain controlled by the attacker.

---

## Question 2 -

What main precondition must exist to enable a CSRF attack against a sensitive function of an application?

**ANSWER -**

In order for a CSRF vulnerability to be exploited the following three conditions must be met:

1. A relevant action must be present – Such as a change e-mail or change password action.

2. The page must use cookie-based session handling – The application relies on cookies for user validation.

3. There should be no unpredictable request parameters – The request parameters values are guessable for instance in a change password function if the current password needs to be present than the function is not vulnerable.

---

## Question 3 -

What three defensive measures can be used to prevent JavaScript hijacking attacks?

**ANSWER -**

1. Having a strong Content-Security Policy.

2. Proper input validation and input sanitization.

3. Use secure-coding practices.

---

## Question 4 -

For each of the following technologies, identify the circumstances, if any, in which the technology would request ```/crossdomain.xml``` to properly enforce domain segregation:

1. Flash

2. Java

3. HTML5

4. Silverlight

**ANSWER -**

1. Flash doesn't exist anymore.

2. Java won't check.

3. HTML5 won't check, because it uses Cross-Origin Resource Sharing instead.

4. Silverlight doesn't exist anymore.

---

## Question 5 -

"We're safe from clickjacking attacks because we don't use frames." What, if anything, is wrong with this statement?

**ANSWER -**

It's not about wether you use frames or not, the frame is used by the *attacker* to embed your webpage into theirs.

---

## Question 6 -

You identify a persistent XSS vulnerability within the display name caption used by an application. This string is only ever displayed to the user who configured it, when they are logged in to the application. Describe the steps that an attack would need to perform to compromise another user of the application.

**ANSWER -**

???

Apparently the answer is:

> (a) The attacker creates his own account on the application, and places a malicious payload into his own display name.

> (b) The attacker creates his own site that causes visitors to log in to the vulnerable application using the attacker's credentials (via a CSRF attack against the login function), and then request the page containing the malicious display name.

> (c) When a victim is induced to visit the attacker's website, she is logged in to the vulnerable application, and the attacker's JavaScript executes. This script persists itself within the victim's browser, logs out of the application, and presents some content that induces the victim to log in using her own credentials. If she does this, then the attacker's script can compromise both the victim's credentials and her resulting session. From the victim's persepective the attack is seamless and appears to involve simply following a link, and then being presented with the vulnerable application's own login function.

---

## Question 7 -

How would you test whether an application allows cross-domain requests using ```XMLHttpRequest```?

**ANSWER -**

By adding an ```Origin``` header and checking wether the value is echoed within the ```Access-Control-Allow-Origin``` response header.

---

## Question 8 -

Describe three ways in which an attacker might induce a victim to use an arbitrary cookie.

**ANSWER -**

1. Cookie injection via URL get request.

2. Cross-Site Scripting.

3. Man-in-the-Middle attacks.
