from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShoppingPage:
    """
    Класс для представления главной страницы магазина.

    Attributes:
    driver (webdriver): Экземпляр веб-драйвера для взаимодействия с браузером.
    """

    def __init__(self, driver):
        """
        Инициализация класса ShoppingPage.

        Args:
        driver (webdriver): Экземпляр веб-драйвера.
        """
        self.driver = driver

    @allure.step("Ожидание загрузки страницы покупок")
    def expectation(self) -> None:
        """Ожидает появления dct[ элементов на странице покупок.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".inventory_item")))

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        """
        Добавляет несколько товаров в корзину и переходит к оформлению заказа.

        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
