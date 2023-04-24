# Chapter 6 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

While testing a web application, you log in using your credentials of ```joe``` and ```pass```. During the login process, you see a request for the following URL appear in your intercepting proxy:

```http://www.wahh-app.com/app?action=login&uname=joe&password=pass```

What three vulnerabilities can you diagnose without probing any further?

**ANSWER -**

The first vulnerability in the URL comes from the use of HTTP instead of HTTPS during the login process. The second vulnerability comes from using a GET request to submit user credentials. The last vulnerability comes from the password itself, it seems that the application allows for the use of weak passwords.

---

## Question 2 -

How can self-registration functions introduce username enumeration vulnerabilities? How can these vulnerabilities be prevented?

**ANSWER -**

Self-registration functions can introduce enumeration vulnerabilities by revealing too much information about existing users, this usually happens by giving messages to the user about wether or not a username is already taken or by refusing to register a certain username. There are two ways this type of vulnerability can be prevented, one is to pick a random unique username _for_ the user and the other is to use an e-mail as the username and e-mail them a registration URL.

---

## Question 3 -

A login mechanism involves the following steps:

1. The application requests the user's username and passcode.

2. The application requests two randomly chosen letters from the user's memorable word.

Why is the required information requested in two seperate steps? What defect would the mechanism contain if this were not the case?

**ANSWER -**

The application does this in order to not load in letters from the memorable word if the users credentials are incorrect. If this were _not_ the case, attackers could continuously refresh the page gettting letters from the memorable word until they know the whole word.

---

## Question 4 -

A multistage login mechanism first requests the user's username and then various other items across successive stages. If any supplied item is invalid, the user is immediately returned to the first stage.

What is wrong with this mechanism, and how can the vulnerability be corrected?

**ANSWER -**

This style of multi-stage login is capable of leaking user information, once a stage is passed it is a confirmation that the supplied data is correct, allowing an attacker to enumerate through the login mechanism. The vulnerability can be corrected by allowing a user to supply data at every stage and only at the end reveal that the login has failed.

---

## Question 5 -

An application incorporates an antiphishing mechanism into its login functionality. During registration, each user selects a specific image from a large bank of memorable images that the application presents to her. The login function involves the following steps:

1. The user enters her username and date of birth.

2. If these details are correct, the application shows the user her chosen image; otherwise, a random image is displayed.

3. The user verifies whether the correct image is displayed. If it is, she enters her password.

The idea behind this antiphishing mechanism is that it enables the user to confirm that she is dealing with the authentic application, not a clone, because only the real application knows the correct image to display to the user.

What vulnerability does this antiphishing mechanism introduce into the login function? Is the mechanism effective at preventing phishing?

**ANSWER -**

This process does not work. An attacker would only need to use the first set of credentials (username and date of birth) twice to verify if the credentials are valid, if the same photo is shown both times an attacker can tell that this user exists.
