# Chapter 9 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

You are trying to exploit a SQL injection flaw by performing a ```UNION``` attack to retrieve data. You do not know how many columns the original query returns. How can you find this out?

**ANSWER -**



---

## Question 2 -

You have located a SQL injection vulnerability in a string parameter. You believe the database is either MS-SQL or Oracle, but you can't retrieve any data or an error message to confirm which database is running. How can you find this out?

**ANSWER -**



---

## Question 3 -

You have submitted a single quotation mark at numerous locations throughout the application. From the resulting error messages you have diagnosed several potential SQL injection flaws. Which one of the following would be the safest location to test whether more crafted input has an effect on the application's processing?

1. Registering a new user.

2. Updating your personal details.

3. Unsubscribing from the service.

**ANSWER -**



---

## Question 4 -

You have found a SQL injection vulnerability in a login function, and you try to input ```' or 1 = 1``` to bypass the login. Your attack fails, and the resulting error message indicates that the ```--``` characters are being stripped by the application's input filters. How could you circumvent this problem?

**ANSWER -**



---

## Question 5 -

You have found a SQL injection vulnerabilty but have been unable to carry out any useful attacks, because the application rejects any input containing whitespace. How can you work around this restriction?

**ANSWER -**

---

## Question 6 -

The application is doubling up all single quotation marks within user input before these are incorporated into SQL queries. Youy have found a SQL injection vulnerability in a numeric field, but you need to use a string value in one of your attack payloads. How can you place a string in your query without using any quotation marks?

**ANSWER -**

---

## Question 7 -

In some rare situations, applications construct dynamic SQL queries from user-supplied input in any way that cannot be made safe using parameterized queries. When does this occur?

**ANSWER -**

---

## Question 8 -

You have escalated privileges within an application such that you now have full administrative access. You discover a SQL injection vulnerability within a user administration function. How can you leverage this vulnerability to further advance your attack?

**ANSWER -**

---

## Question 9 -

You are attacking an application that holds no sensitive data and contains no authentication or access control mechanisms. In this situation, how should you rank the significance of the following vulnerabilities?

1. SQL Injection

2. XPath Injection

3. OS Command Injection

**ANSWER -**

---

## Question 10 -

You are probing an application function that enables you to search personel details. You suspect that the function is accessing either a database or an Active Directory back end. How could you try to determine which of these is the case?

**ANSWER -**
