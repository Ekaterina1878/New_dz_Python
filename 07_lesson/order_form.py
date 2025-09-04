from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def form(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Ekaterina")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Morozova")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("195298")

    def button_continui(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".cart_item")))

    def price(self):
        price_total = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        return float(price_total.split("$")[1])
