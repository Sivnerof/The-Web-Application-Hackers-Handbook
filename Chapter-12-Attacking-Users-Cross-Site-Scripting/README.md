# Chapter 12 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

What standard "signature" in an application's behavior can be used to identify most instances of XSS vulnerabilities?

**ANSWER -**

User-supplied data is presented within the application unmodified.

---

## Question 2 -

You discover a reflected XSS vulnerability within the unauthorized area of an application's functionality. State two different ways in which the vulnerability could be used to compromise an authenticated session within the application.

**ANSWER -**

A reflected XSS vulnerability can be used in an unauthorized area, such as a login, to keylog the data provided into the login form.

---

## Question 3 -

You discover that the contents of a cookie parameter are copied without any filters or sanitization into the application's response. Can this behavior be used to inject arbitrary JavaScript into the returned page? Can it be exploited to perform an XSS attack against another user?

**ANSWER -**

Yes, cookies are a potential vector for XSS attacks and it is technically possible to attack other users but only if the cookie is reflected in other parts of the application like a URL.

---

## Question 4 -

You discover stored XSS behavior within data that is only ever displayed back to yourself. Does this behavior have any security significance? 

**ANSWER -**

If the data is *only* displayed back to yourself then the vulnerability can only be leveraged to attack *other* users if it is chained with other vulnerabilities.

---

## Question 5 -

You are attacking a web mail application that handles file attachments and displays these in-browser. What common vulnerability should you immediately check for?

**ANSWER -**

XSS vulnerabilities can be found within many web mail applications, so one thing to check for in this situation is whether JavaScript can be executed within an HTML file that is sent to another user.

---

## Question 6 -

How does the same-origin policy impinge upon the use of the Ajax technology ```XMLHttpRequest```?

**ANSWER -**

```XMLHttpRequest``` can now be used to make cross-site requests.

---

## Question 7 -

Name three possible attack payloads for XSS exploits (that is, the malicious actions that you can perform within another user's browser, not the methods by which you deliver the attacks).

**ANSWER -**

1. Keylogging

2. Stealing Cookies

3. Causing a user to execute actions they did not intend to.

---

## Question 8 -

You have discovered a reflected XSS vulnerability where you can inject arbitrary data into a single location within the HTML of the returned page. The data inserted is truncated to 50 bytes, but you want to inject a lengthy script. You prefer not to call out to a script on an external server. How can you work around the length limit?

**ANSWER -**

By using DOM based XSS.
