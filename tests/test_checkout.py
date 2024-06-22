from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

import json

def test_checkout(_browser):

    URL = "https://www.saucedemo.com/"
    wait = WebDriverWait(_browser, 10)

    # Open json file
    with open('./data/test_data.json', 'r') as JF:
        json_data = json.load(JF)

    _browser.maximize_window()

    # Initiale class objects
    login_page = LoginPage(_browser)
    home_page = HomePage(_browser)
    cart_page = CartPage(_browser)
    product_page = ProductPage(_browser)
    checkout_page = CheckoutPage(_browser)

    # Login
    login_page.open_page(URL)
    login_page.login(json_data["login"]["username"], json_data["login"]["password"])
    
    home_page.open_home(wait)

    # Buy product
    product_page.open_product(wait, json_data["products"][0]["product_name"])
    product_page.buy_product(wait) 
    
    # Get price on product page
    product_price = product_page.get_product_details(wait)[1]
    
    # Go to home page
    home_page.open_cart(wait)

    # Procceed to checkout
    cart_page.buy_product(wait)

    # Insert user data
    checkout_page.insert_data(wait, json_data["user"]["first_name"], json_data["user"]["last_name"], json_data["user"]["postal_code"])
    
    # Get price of product, tax and total price
    total_prices = checkout_page.get_total_cost(wait)

    assert float(product_price) == total_prices[0]

    assert round(float(product_price) * .08, 2) == total_prices[1]

    assert round(float(product_price) * .08, 2) + float(product_price) == total_prices[2]