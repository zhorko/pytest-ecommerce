from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
import json

from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_products(_browser):

    URL = "https://www.saucedemo.com/"
    wait = WebDriverWait(_browser, 10)

    # Open json file
    with open('./data/test_data.json', 'r') as JF:
        json_data = json.load(JF)

    _browser.maximize_window()

    # Logging in
    login_page = LoginPage(_browser)
    login_page.open_page(URL)
    login_page.login(json_data["login"]["username"], json_data["login"]["password"])

    # Getting all products from page
    home_page = HomePage(_browser)
    actual_prods = home_page.get_products(wait)

    # Iterating through products 
    for index, item in enumerate(json_data["products"]):
        assert json_data["products"][index]["product_name"] in actual_prods