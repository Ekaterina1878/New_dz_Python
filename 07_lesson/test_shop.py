import pytest
from selenium import webdriver
from autorize import AuthorizationPage
from shopping_page import ShoppingPage
from cart_page import CartPage
from order_form import FormPage


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
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
    assert price_value == 58.29, f"Ожидали 58.29, но получили {price_value}"
