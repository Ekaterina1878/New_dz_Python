import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации веб-драйвера.

    Returns:
        webdriver: Экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Проверка функциональности калькулятора " \
                    "с использованием Selenium и Allure.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    """
    Тест для проверки работы калькулятора.

    Args:
        driver (webdriver): Экземпляр веб-драйвера.

    Returns:
        None
    """
    Calculator_page = CalculatorPage(driver)
    Calculator_page.open()
    Calculator_page.delay()
    Calculator_page.click_button()
    Calculator_page.expectation()
    res = Calculator_page.result()
    with allure.step("Проверка результата"):
        assert res == "15"
