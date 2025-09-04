import pytest
from selenium import webdriver
from Calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    Calculator_page = CalculatorPage(driver)
    Calculator_page.open()
    Calculator_page.delay()
    Calculator_page.click_button()
    Calculator_page.expectation()
    res = Calculator_page.result()
    assert res == "15"
