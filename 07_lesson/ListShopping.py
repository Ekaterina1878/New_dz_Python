from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingPage:
    def __init__(self, driver):
        self.driver = driver

    def expectation(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".inventory_item")))

    def add_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
