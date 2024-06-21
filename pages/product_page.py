from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def open_product(self, wait, product_name):
        # Open product page
        try:
            wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '"+ product_name +"')]/.."))
            ).click()
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('products', e))

    def get_product_details(self, wait):
        # Find name
        try:
            name = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='inventory-item-name']"))
            ).text
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('products', e))

        # Find price
        try:
            price = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='inventory-item-price']"))
            )
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('products', e))

        # Find description
        try:
            desc = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='inventory-item-desc']"))
            ).text
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('products', e))

        if '$' in price.text:
            price = price.text.replace('$', '')

        return [name, price, desc]
    
    def buy_product(self, wait):
        # Add to cart
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn_inventory"))
            ).click()
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('products', e))
        