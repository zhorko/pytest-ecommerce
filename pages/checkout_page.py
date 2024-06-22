from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def insert_data(self, wait, username, usersurname, postal):
        # Fill in user information 
        try:
            data_table = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".checkout_info input"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('product_quant', e))

        data_table[0].send_keys(username)
        data_table[1].send_keys(usersurname)
        data_table[2].send_keys(postal)
        
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button").click()

    def get_total_cost(self, wait):

        try:
            subtotal_price = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_subtotal_label"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('subtotal_price', e))

        try:
            tax = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_tax_label"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('tax', e))

        try:
            total_price = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('product_quant', e))

        subtotal_price = subtotal_price.text.replace("Item total: $", "")
        tax = tax.text.replace("Tax: $", "")
        tax = tax[:-1]
        total_price = total_price.text.replace("Total: $", "")
        
        return float(subtotal_price), float(tax), float(total_price)
    
    def finish_buy(self, wait):

        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_button"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('finish_buy', e))