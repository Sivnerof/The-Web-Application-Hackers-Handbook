# Chapter 3 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

What is the ```OPTIONS``` method used for?

**ANSWER -**

The ```OPTIONS``` method is used in an HTTP request to solicit information from the server as to what HTTP methods are allowed.

---

## Question 2 -

What are the ```If-Modified-Since``` and ```If-None-Match``` headers used for? Why might you be interested in these when attacking an application?

**ANSWER -**

The ```If-Modified-Since``` header is used to check whether or not a resource requested through a ```GET``` method has changed since the date sent in the ```If-Modified-Since``` value. If it has, the server responds with the ```200``` status code and sends the new resource. If the resource has not changed since the date provided, then the server responds with a ```304``` status code and nothing is sent in the HTTP response body, while the resource is grabbed from the local cache.

The ```If-None-Match``` header is sent by the client to the server to check whether a resources ```E-Tag``` matches the one sent. If the ```E-Tag``` in the ```If-None-Match``` value field is identical to the one stored on the server, the server will respond with a ```304``` status code and an empty body, while the resource is grabbed from the local cache. If the ```E-Tag``` is different then the resource is fetched from the server along with a new ```E-Tag```.

An important thing to note about the use of the ```E-Tag``` is that some servers will use this to track you without using cookies.

One reason an attacker may be interested in these headers is that they may be trying to put more stress on the server by causing it to continuosly resending resources by stripping the two headers from their requests or they may be trying to get fresh versions of the resources.

---

## Question 3 -

What is the significance of the ```secure``` flag when a server sets a cookie?

**ANSWER -**

The ```secure``` flag is specified by a server to tell a client that this cookie can only be sent via HTTPS. This security mechanism is used to safeguard the cookies from man in the middle attacks.

---

## Question 4 -

What is the difference between the common status codes ```301``` and ```302```?

**ANSWER -**

The ```301``` status code ("Moved Permanently") is sent by a server in response to a request for a resource that has since been moved to a different location, the new resource can be found within the ```Location``` header of the HTTP response.

The ```302``` status code ("Found") is sent by a server in response to a request for a resource that has _temporarily_ moved. This response is usually given while a site is under maintenance or for testing purposes and implies that the resource requested can be visited at the original requested URL at some time in the future.

Both ```301``` and ```302``` status codes are part of the redirect family of status codes, the difference between the two is that one is used for permanent redirects (```301```) and the other is used for temporary redirects (```302```).

---

## Question 5 -

How does a browser interoperate with a web proxy when ```SSL``` is being used?

**ANSWER -**

The clients browser will send an HTTP ```CONNECT``` request to the proxy with the domain name and port number, if accepted the proxy will respond with a ```200``` status code and forward requests to the destination via the proxy.
