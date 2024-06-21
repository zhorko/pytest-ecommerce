from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver

    def get_products(self, wait):
        product_names = []
        
        try:
            products = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".inventory_list .inventory_item_name"))
            )
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('products', e))

        for e in products:
            product_names.append(e.text)

        return product_names