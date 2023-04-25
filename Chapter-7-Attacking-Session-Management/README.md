# Chapter 7 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

You log in to an application, and the server sets the following cookie:

```http
Set-cookie: sessid=amltMjM6MTI0MToxMTk0ODcwODYz;
```

An hour later, you log in again and receive the following:

```http
Set-cookie: sessid=amltMjM6MTI0MToxMTk0ODc1MTMy;
```

What can you deduce about these cookies?

**ANSWER -**

Decoding the cookies from their ```Base64``` encoding reveals the following:

1. ```jim23:1241:1194870863```

2. ```jim23:1241:1194875132```

From these decoded cookies we can tell that the cookie is broken into three pieces of data. Two of which are constant values, while only the third piece of data changes. We can infer the following information from the three pieces of data:

1. ```jim23``` - Appears to be the current users username.

2. ```1241``` - The second constant value, we can guess this is probably a user id.

3. ```1194870863/1194875132``` - The only changing piece of data, **increments** by 4269. This piece of data appears to be time based and the number 4269 when converted from seconds to hours is a little over an hour, which matches the hour long time difference between when the two requests were made. Decoding these two pieces of data which happen to be Unix Time Stamps, we'll get the following dates:

    * ```Mon 12 November 2007 12:34:23 UTC```

    * ```Mon 12 November 2007 13:45:32 UTC```

---

## Question 2 -

An application employs six-character alphanumeric session tokens and five-character alphanumeric passwords. Both are randomly generated according to an unpredictable algorithm. Which of these is likely to be the more worthwhile target for a brute-force guessing attack? List all the different factors that may be relevant to your decision.

**ANSWER -**

Both methods have their benefits/downsides. Cracking passwords involves also knowing the usernames so you'll need to enumerate users and passwords which might be time consuming _but_ you will be able to take over a non logged in user. In the case of session tokens it may be faster to enumerate tokens due to the fact that tokens are one character shorter than passwords, but you can only hijack active sessions, so non logged in users will not be effected. Also the initial payout might be lower due to high success rates depending on high amount of logged in users. 

---

## Question 3 -

You log in to an application at the following URL:

```https://foo.wahh-app.com/login/home.php```

The server sets the following cookie:

```http
Set-cookie: sessionId=1498172056438227; domain=foo.wahh-app.com; path=/login; HttpOnly;
```

You then visit a range of other URLs. To which of the following will your browser submit the ```sessionId``` cookie? (Select all that apply.)

1. ```https://foo.wahh-app.com/login/myaccount.php```

2. ```http://bar.wahh-app.com/login```

3. ```https://staging.foo.wahh-app.com/login/home.php```

4. ```http://foo.wahh-app.com/login/myaccount.php```

5. ```http://foo.wahh-app.com/logintest/login.php```

6. ```https://foo.wahh-app.com/logout```

7. ```https://wahh-app.com/login/```

8. ```https://xfoo.wahh-app.com/login/myaccount.php```

**ANSWER -**

1. Yes, the domain and subdomain match the requirements, and the resource requested is within the ```/login``` directory.

2. No, ```bar``` is a completely different subdomain and it does not matter that the path set by the cookie matches the path in this URL.

3. Yes, ```staging``` is a subdomain of the subdomain ```foo``` and the resource requested exists within the correct path.

4. Yes, the resource requested exists within the correct path (```/login```).

5. Yes, because the cookie path (```/login```) does not end in ```/``` so the path ```/logintest``` will also have the cookie set.

6. No, the ```/logout``` path does not match ```/login```.

7. No, this is the parent domain of ```foo``` and the cookie specifically states it should be set in the _subdomain_ named ```foo```.

8. No, this is a different subdomain, it may appear similar to ```foo``` but this subdomain is prefixed with the letter ```x```.

---

## Question 4 -

The application you are targetting uses per-page tokens in addition to the primary session token. If a per-page token is received out of sequence, the entire session is invalidated. Suppose that you discover some defect that enables you to predict or capture the tokens issued to other users who are currently accessing the application. Can you hijack their sessions?

**ANSWER -**

Yes, you could still hijack the session but you're actions will be very limited.

---

## Question 5 -

You log in to an application, and the server sets the following cookie:

```http
Set-cookie: sess=ab11298f7eg14;
```

When you click the logout button, this causes the following client-side script to execute:

```js
document.cookie="sess=";
document.location="/";
```

What conclusion would you draw from this behavior?

**ANSWER -**

The above code tells me that session cookies are being invalidated with JavaScript, meaning that there is a strong chance that old sessions are still stored on the server. A user can verify the vulnerability by saving their cookie and trying to reuse it after logging out.
