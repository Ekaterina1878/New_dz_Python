from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """
    Класс CartPage для представления страницы корзины.

    Attributes:
    driver (webdriver): Экземпляр веб-драйвера для взаимодействия с браузером.
    """

    def __init__(self, driver):
        """
        Инициализация класса CartPage.

        Args:
        driver (webdriver): Экземпляр веб-драйвера.
        """

        self.driver = driver

    @allure.step("Ожидание загрузки страницы корзины")
    def expect(self) -> None:
        """Ожидает открытия страницы с содержимым корзины."""

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#cart_contents_container")))

    @allure.step("Нажатие на кнопку 'Checkout' для оформления заказа")
    def button_checkout(self) -> None:
        """Нажимает кнопку 'Checkout' для перехода к форме заказа.

        : return: None
        """

        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
