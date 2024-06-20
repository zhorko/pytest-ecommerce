from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
import json

from pages.login_page import LoginPage


def test_login(_browser):
    
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

    # Verifying successfull login by finding "Logout" button
    _browser.find_element(By.CSS_SELECTOR, "button[id='react-burger-menu-btn']").click() 
    try:
        logout = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='logout_sidebar_link'"))
        )
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('logout', e))

    assert logout.text == "Logout"