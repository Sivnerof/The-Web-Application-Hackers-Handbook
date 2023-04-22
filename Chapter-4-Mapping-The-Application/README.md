# Chapter 4 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

While mapping an application, you encounter the following URL:

```https://wahh-app.com/CookieAuth.dll?GetLogon?curl=Z2Fdefault.aspx```

What information can you deduce about the technologies employed on the server and how it is likely to behave?

**ANSWER -**



---

## Question 2 -

The application you are targetting implements web forum functionality. Here is the only URL you have discovered:

```http://wahh-app.com/forums/ucp.php?mode=register```

How might you obtain a listing of forum members?

**ANSWER -**



---

## Question 3 -

While mapping an application, you encounter the following URL:

```https://wahh-app.com/public/profile/Address.asp?action=view&location=default```

What information can you infer about server-side technologies? What can you conjecture about other content and functionality that may exist?

**ANSWER -**



---

## Question 4 -

A web server's responses include the following header:

```http
Server: Apache-Coyote/1.1
```

What does this indicate about the technologies in use on the server?

**ANSWER -**



---

## Question 5 -

You are mapping two different web applications, and you request the URL ```/admin.cpf``` from each application. The response headers returned by each request are shown here. From these headers alone, what can you deduce about the presence of the requested resource within each application?

```http
HTTP/1.1 200 OK
Server: Microsoft-IIS/5.0
Expires: Mon, 20 Jun 2011 14:59:21 GMT
Content-Location: http://wahh-app.com/includes/error.htm?404;http://wahh-app.com/admin.cpf
Date: Mon, 20 Jun 2011 14:59:21 GMT
Content-Type: text/html
Accept-Ranges: bytes
Content-Length: 2117

HTTP/1.1 401 Unauthorized
Server: Apache-Coyote/1.1
WWW-Authenticate: Basic realm="Wahh Administration Site"
Content-Type: text/html;charset=utf-8
Content-Length: 954
Date: Mon, 20 Jun 2011 15:07:27 GMT
Connection: close
```

**ANSWER -**
