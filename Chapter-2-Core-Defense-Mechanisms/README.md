# Chapter 2 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

Why are an application's mechanisms for handling user access only as strong as the weakest of these components?

**ANSWER -**

As long as an attacker is able to exploit a vulnerability within any link in the user access chain then it does not matter how strong the other links are because the attacker has already gained the ability to masquerade as other users.

---

## Question 2 -

What is the difference between a session and a session token?

**ANSWER -**

A session is information stored on a server about a users current state, for example, what items appear in your shopping cart or what the users preferences are. Session tokens on the other hand are used to label what sessions belong to what users.

---

## Question 3 -

Why is it not always possible to use a whitelist-based approach to input validation?

**ANSWER -**

Whitelist-based approaches to input validation may be extremely limiting and user inputs will not always match 100 percent with what a developer may expect. This may lead to a frustrating user experience.

---

## Question 4 -

You are attacking an application that implements an administrative function. You do not have any valid credentials to use the function. Why should you nevertheless pay close attention to it?

**ANSWER -**

Even though we may not have the appropriate credentials to use the function there is still the possibility that a vulnerability exists within the function that we may be able to leverage.

---

## Question 5 -

An input validation mechanism designed to block cross-site scripting attacks performs the following sequence of steps on an item of input:

1. Strip any ```<script>``` expressions that appear.

2. Truncate the input to 50 characters.

3. Remove any quotation marks within the input.

4. URL-decode the input.

5. If any items were deleted, return to step 1.

Can you bypass this validation mechanism to smuggle the following data past it?

```"><script>alert("foo")</script>```

**ANSWER -**

We can abuse the logic of the above validation mechanism by URL encoding the quotation marks and the opening angle bracket.

```js
%22>%3Cscript>alert(%22foo%22)</script>
```

This will bypass step one because there is no ```<script>``` tag. Step 2 is bypassed because there are only 38 characters. Step 3 is bypassed because the quotation marks are URL encoded. Step 4 is executed causing our payload to come together. Step 5 is bypassed because nothing was ever deleted.
