# Chapter 4 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

While mapping an application, you encounter the following URL:

```https://wahh-app.com/CookieAuth.dll?GetLogon?curl=Z2Fdefault.aspx```

What information can you deduce about the technologies employed on the server and how it is likely to behave?

**ANSWER -**

The ```CookieAuth.dll``` file is used in Microsoft's Internet Information Services (IIS) to provide cookie based authorization, so it appears that this URL is setting a cookie by calling the ```GetLogon``` method and if the login is successfull the user will be rerouted to the websites default home page named ```Z2default.aspx``` by using the ```curl``` command.

---

## Question 2 -

The application you are targetting implements web forum functionality. Here is the only URL you have discovered:

```http://wahh-app.com/forums/ucp.php?mode=register```

How might you obtain a listing of forum members?

**ANSWER -**

The "```ucp```" in ```ucp.php``` stands for "User Control Panel" and this file is used in the ```phpBB``` forum software to configure user settings, the fact that ```phpBB``` is used might mean that there may also be a ```memberlist.php``` file that lists all registered forum users.

---

## Question 3 -

While mapping an application, you encounter the following URL:

```https://wahh-app.com/public/profile/Address.asp?action=view&location=default```

What information can you infer about server-side technologies? What can you conjecture about other content and functionality that may exist?

**ANSWER -**

This URL is using the ```.asp``` file extension (Active Server Page) so we know that this website is using ```ASP.NET``` to generate dynamic web pages. It also seems that this URL implies the existence of a ```/private``` directory. The ```Address.asp``` file is also being called with the parameters ```action``` and ```location``` with the values ```view``` and ```default```, this might imply that other methods exist like ```delete``` or ```create``` and that ```default``` might be a directory on the server, so this might be leveraged by an attacker to view other directories.

---

## Question 4 -

A web server's responses include the following header:

```http
Server: Apache-Coyote/1.1
```

What does this indicate about the technologies in use on the server?

**ANSWER -**

This means that the server is running Apache Tomcat. It's also important to note that the information sent by the server isn't always accurate or up to date.

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

Looking at the first response we can see that the server sent a ```200``` status code, this might seem like the resource exists but looking closer at the ```Content-Location``` header we can see that this page was dynamically created by the server (```http://wahh-app.com/includes/error.htm?404```) so the resource we're looking for was not actually found.

In the second HTTP response we can see that the server responded with a ```401``` status code, indicating that the resource does exist but we are not authorized to view this resource. We can also verify this by viewing the ```WWW-Authenticate``` header in the response.
