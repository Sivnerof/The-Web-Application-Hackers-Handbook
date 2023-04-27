# Chapter 10 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

A network device provides a web-based interface for performing device configuration. Why is this kind of functionality often vulnerable to OS command injection attacks?

**ANSWER -**



---

## Question 2 -

You are testing the following URL:

```http://wahh-app.com/home/statsmgr.aspx?country=US```

Changing the value of the ```country``` parameter to ```foo``` results in the error message:

```Could not open file: D:\app\default\home\logs\foo.log (invalid file).```

What steps could you take to attack the application?

**ANSWER -**



---

## Question 3 -

You are testing an AJAX application that sends data in XML format within POST requests. What kind of vulnerability might enable you to read arbitrary files from the server's filesystem? What prerequisites must be in place for your attack to succeed?

**ANSWER -**



---

## Question 4 -

You make the following request to an application that is running on the ASP.NET platform:

```http
POST /home.aspx?p=urlparam1&p=urlparam2 HTTP/1.1
Host: wahh-app.com
Cookie: p=cookieparam
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

p=bodyparam
```

The application executes the following code:

```String param = Request.Params["p"];```

What value does the ```param``` variable have?

**ANSWER -**



---

## Question 5 -

Is HPP a prerequisite for HPI, or vice versa?

**ANSWER -**



---

## Question 6 -

An application contains a function that proxies requests to external domains and returns the responses from these requests. To prevent server-side redirection attacks from retrieving protected resources on the application's own web server, the application blocks requests targetting ```localhost``` or ```127.0.0.1```. How might you circumvent this defense to access resources on the server?

**ANSWER -**



---

## Question 7 -

An application contains a function for user feedback. This allows the user to supply their e-mail address, a message subject, and detailed comments. The application sends an e-mail to ```feedback@wahh-app.com```, addressed from the user's e-mail address, with the user-supplied subject line and comments in the message body. Which of the following is a valid defense against mail injection attacks?

1. Disable mail relaying on the mail server.

2. Hardcode the ```RCPT TO``` field with ```feedback@wahh-app.com```.

3. Validate that the user-supplied inputs do not contain any newlines or other SMTP metacharacters.

**ANSWER -**

