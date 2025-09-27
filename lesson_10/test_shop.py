import pytest
from selenium import webdriver
from authorize import AuthorizationPage
from shopping_page import ShoppingPage
from cart_page import CartPage
from order_form import FormPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации драйвера Selenium.

    :return: webdriver.Firefox, экземпляр драйвера Firefox.
    """
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест страницы оформления заказа")
@allure.description("Проверка процесса оформления заказа на сайте")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver) -> None:
    """
    Тест для проверки процесса оформления заказа.

    :param driver: webdriver.Firefox, экземпляр драйвера Selenium.
    :return: None
    """
    auth = AuthorizationPage(driver)
    auth.open()
    auth.authorize()
    shop = ShoppingPage(driver)
    shop.expectation()
    shop.add_to_cart()
    cart_check = CartPage(driver)
    cart_check.expect()
    cart_check.button_checkout()
    form_input = FormPage(driver)
    form_input.form()
    form_input.button_continui()
    form_input.price()
    price_value = form_input.price()
    with allure.step("Проверка общей цены"):
        assert price_value == 58.29, (
            f"Ожидали 58.29, нополучили {price_value}")
