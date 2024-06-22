from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

import json


def test_cart(_browser):

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

    # Log in
    login_page.open_page(URL)
    login_page.login(json_data["login"]["username"], json_data["login"]["password"])
    
    home_page.open_home(wait)

    # Buy product
    product_page.open_product(wait, json_data["products"][0]["product_name"])
    product_page.buy_product(wait) 
    
    # Go to home page
    home_page.open_home(wait)
    
    # Get number of items in cart
    cart_old_num = home_page.get_cart_quantity(wait)
    
    # Buy product
    product_page.open_product(wait, json_data["products"][1]["product_name"])
    product_page.buy_product(wait)

    # Get number of items in cart
    cart_new_num = home_page.get_cart_quantity(wait)
    assert cart_old_num < cart_new_num
    
    # Go to home page
    home_page.open_cart(wait)
    
    # Get number of items in cart
    cart_size_many = cart_page.get_cart_quantity(wait)

    # Check number of each product added
    assert cart_page.get_product_quantity(wait, 0) == 1
    assert cart_page.get_product_quantity(wait, 1) == 1

    # Validate product names from database
    assert cart_page.get_product_data(wait, 0)[0] == json_data["products"][0]["product_name"]
    assert cart_page.get_product_data(wait, 1)[0] == json_data["products"][1]["product_name"]

    # Validate product prices from database
    assert cart_page.get_product_data(wait, 0)[1] == json_data["products"][0]["expected_price"]
    assert cart_page.get_product_data(wait, 1)[1] == json_data["products"][1]["expected_price"]

    # Remove one product
    cart_page.remove_product(wait, 0)
    cart_size_less = cart_page.get_cart_quantity(wait)

    # Validate that number of items in cart did change
    assert cart_size_less < cart_size_many