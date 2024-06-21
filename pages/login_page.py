from selenium.webdriver.common.by import By

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    # Click on existing category name 
    def login(self, json_username, json_password):
        self.driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(json_username)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(json_password)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()