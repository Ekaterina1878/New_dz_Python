from selenium.webdriver.common.by import By


class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorize(self):
        self. driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
