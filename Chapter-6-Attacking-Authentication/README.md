# Chapter 6 Questions And Answers

**NOTE** - The answers in this README file are mine and may not be completely correct. The **official** solutions can be found by using [The Wayback Machine](https://web.archive.org/ "The WayBack Machine Website") on the following link http://mdsec.net/wahh/answers2e.html, or clicking the link below.

https://web.archive.org/web/20190210210741/http://mdsec.net/wahh/answers2e.html

---

## Question 1 -

While testing a web application, you log in using your credentials of ```joe``` and ```pass```. During the login process, you see a request for the following URL appear in your intercepting proxy:

```http://www.wahh-app.com/app?action=login&uname=joe&password=pass```

What three vulnerabilities can you diagnose without probing any further?

**ANSWER -**



---

## Question 2 -

How can self-registration functions introduce username enumeration vulnerabilities? How can these vulnerabilities be prevented?

**ANSWER -**



---

## Question 3 -

A login mechanism involves the following steps:

1. The application requests the user's username and passcode.

2. The application requests two randomly chosen letters from the user's memorable word.

Why is the required information requested in two seperate steps? What defect would the mechanism contain if this were not the case?

**ANSWER -**



---

## Question 4 -

A multistage login mechanism first requests the user's username and then various other items across successive stages. If any supplied item is invalid, the user is immediately returned to the first stage.

What is wrong with this mechanism, and how can the vulnerability be corrected?

**ANSWER -**



---

## Question 5 -

An application incorporates an antiphishing mechanism into its login functionality. During registration, each user selects a specific image from a large bank of memorable images that the application presents to her. The login function involves the following steps:

1. The user enters her username and date of birth.

2. If these details are correct, the application shows the user her chosen image; otherwise, a random image is displayed.

3. The user verifies whether the correct image is displayed. If it is, she enters her password.

The idea behind this antiphishing mechanism is that it enables the user to confirm that she is dealing with the authentic application, not a clone, because only the real application knows the correct image to display to the user.

What vulnerability does this antiphishing mechanism introduce into the login function? Is the mechanism effective at preventing phishing?

**ANSWER -**
