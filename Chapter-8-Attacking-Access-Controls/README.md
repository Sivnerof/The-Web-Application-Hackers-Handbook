# Chapter 8 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

An application may use the HTTP ```Referer``` header to control access without any overt indication of this in its normal behavior. How can you test for this weakness?

**ANSWER -**

One way to test if the website you are currently visiting is using the ```Referer``` header to provide some sort of functionality is by stripping the header and resubmitting requests to the website and monitoring any differences in the functionality.

---

## Question 2 -

You log in to an application and are redirected to the following URL:

```https://wahh-app.com/MyAccount.php?uid=1241126841```

The application appears to be passing a user identifier to the ```MyAccount.php``` page. The only identifier you are aware of is your own. How can you test whether the application is using this parameter to enforce access controls in an unsafe way?

**ANSWER -**

You can try logging in as a new user and replacing the new ```uid``` to ```1241126841```, if the page is accessed then it is vulnerable. You can also try to check for other users by iterating different ```uid``` values.

---

## Question 3 -

A web application on the Internet enforces access controls by examining users' source IP addresses. Why is this behavior potentially flawed?

**ANSWER -**

Users can use a VPN, spoof their IP address, or be using a proxy so it's not entirely safe to be relying on an IP address to enforce access controls.

---

## Question 4 -

An application's sole purpose is to provide a searchable repository of information for use by numbers of the public. There are no authentication or session-handling mechanisms. What access controls should be implemented within the application?

**ANSWER -**

Users should be restricted to read-only permissions.

---

## Question 5 -

When browsing an application, you encounter several sensitive resources that need to be protected from unauthorized access and that have the ```.xls``` file extension. Why should these immediately catch your attention?

**ANSWER -**

The ```.xls``` file extension is used for Excel Spreadsheets and may contain sensitive information such as financial records, transactions, and user information. These files are also static so they _may_ be unprotected.
