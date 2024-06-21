from selenium.webdriver.support.wait import WebDriverWait
import json

from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_products(_browser):

    URL = "https://www.saucedemo.com/"
    wait = WebDriverWait(_browser, 10)
    all_correct = False

    # Open json file
    with open('./data/test_data.json', 'r') as JF:
        json_data = json.load(JF)

    _browser.maximize_window()

    # Logging in
    login_page = LoginPage(_browser)
    login_page.open_page(URL)
    login_page.login(json_data["login"]["username"], json_data["login"]["password"])

    # Opening product page
    product_page = ProductPage(_browser)
    product_page.open_product(wait, json_data["products"][1]["product_name"])
    product_details = product_page.get_product_details(wait)

    
    # Iterating through products 
    for index, item in enumerate(json_data["products"]):
        if json_data["products"][index]["product_name"] not in product_details[0]:
            continue
        
        all_correct = True

        if all_correct:
            break
    
    assert all_correct