from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def expect(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#cart_contents_container")))

    def button_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
