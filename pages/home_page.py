from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open_home(self, wait):
        # Open list of products
        self.driver.find_element(By.CSS_SELECTOR, "button[id='react-burger-menu-btn']").click() 
        
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='inventory_sidebar_link'"))
            ).click()
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('go_home', e))

    def open_cart(self, wait):
        # Open cart page
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.shopping_cart_link"))
            ).click()
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('go_home', e))

    def get_cart_quantity(self, wait):
        # Find number at cart icon
        try:
            cart_num = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.shopping_cart_badge"))
            ).text
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('cart_num', e))

        if cart_num is not None:
            return int(cart_num)
        else:
            return None