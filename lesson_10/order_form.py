from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    """
    Класс FormPage представляет страницу оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализация класса FormPage.

        Args:
        driver (webdriver): Экземпляр веб-драйвера.
        """
        self.driver = driver

    @allure.step("Заполнение формы заказа")
    def form(self) -> None:
        """Заполняет форму заказа с предустановленными данными.

        Вводит имя, фамилию и почтовый код.

        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Ekaterina")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Morozova")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("195298")

    @allure.step("Нажатие кнопки 'Continue' для оформления заказа")
    def button_continui(self) -> None:
        """Нажимает кнопку 'Continue' для перехода к следующему шагу.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".cart_item")))

    @allure.step("Получение общей суммы заказа")
    def price(self) -> float:
        """Получает общую цену из формы заказа.

        Returns:
        float: Общая цена заказа.
        """
        price_total = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        return float(price_total.split("$")[1])
