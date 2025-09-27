from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """
    Класс для представления страницы калькулятора.

    Attributes:
        driver (webdriver): Экземпляр веб-драйвера для

        взаимодействия с браузером.
    """

    def __init__(self, driver):
        """
        Инициализация класса CalculatorPage.

        Args:
            driver (webdriver): Экземпляр веб-драйвера для

            взаимодействия с браузером.
        """
        self.driver = driver
        driver.maximize_window()

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-"
            "java/slow-calculator.html")

    @allure.step("Установка задержки в калькуляторе")
    def delay(self) -> None:
        """
        Делает расчет на странице калькулятора, выполня задержку.

        Returns:
            None
        """
        input_delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear()
        input_delay.send_keys("45")

    @allure.step("Нажатие кнопок калькулятора")
    def click_button(self) -> None:
        """
        Нажимает на кнопки калькулятора для выполнения арифметической операции.

        Returns:
            None
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Ожидание результата")
    def expectation(self) -> None:
        """
        Ожидает появления результата на странице калькулятора.

        Returns:
            None
        """
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen")))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Получение результата")
    def result(self) -> str:
        res = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res
