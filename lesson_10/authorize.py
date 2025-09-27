from selenium.webdriver.common.by import By
import allure


class AuthorizationPage:
    """
    Класс AuthorizationPage представляет страницу входа в систему.

    Attributes:

    driver (webdriver): Экземпляр веб-драйвера для взаимодействия с браузером.
    """

    def __init__(self, driver):
        """
        Инициализация класса AuthorizationPage.

        Args:
        driver (webdriver): Экземпляр веб-драйвера.
        """

        self.driver = driver
        driver.maximize_window()

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """

        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя")
    def authorize(self) -> None:
        """

        Находит поля ввода для имени пользователя и пароля,

        вводит данные и нажимает кнопку входа.

        :return: None
        """
        self. driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
