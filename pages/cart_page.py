from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_cart_quantity(self, wait):
        try:
            cart_elements = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.cart_list > div"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('cart_elements', e))

        return len(cart_elements) - 2

    def get_product_data(self, wait, prod_num: int):
        prod_num += 3
        
        try:
            prod_name = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list div:nth-of-type("+ str(prod_num) +") .inventory_item_name"))
            ).text
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('prod_name', e))

        try:
            prod_price = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list div:nth-of-type("+ str(prod_num) +") .inventory_item_price"))
            ).text
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('prod_price', e))

        prod_price = prod_price.replace('$', '')

        return [prod_name, prod_price]
        
    def get_product_quantity(self, wait, prod_num: int):
        prod_num += 3

        try:
            product_quant = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list div:nth-of-type("+ str(prod_num) +") .cart_quantity"))
            ).text
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('product_quant', e))

        return int(product_quant)

    def buy_product(self, wait):
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".checkout_button"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('buy_prod', e))

    def remove_product(self, wait, prod_num):
        prod_num += 3
        
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list div:nth-of-type("+ str(prod_num) +") .cart_button"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('prod_remover', e))

        self.driver.refresh()