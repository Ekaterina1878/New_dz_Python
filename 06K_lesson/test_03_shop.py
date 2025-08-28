import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping(driver):
    driver.get("https://www.saucedemo.com/")

# Авторизация
    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()

    # Ожидание загрузки  страницы
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, ".inventory_item")))

    # Добавление товара в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "#cart_contents_container")))
    # Кнопка Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение формы
    driver.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Ekaterina")
    driver.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Morozova")
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("195298")

    # Нажатие на кнопку Contunie
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, ".cart_item")))

    # Чтение итоговой стоимости
    price_total = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text
    price_value = float(price_total.split("$")[1])
    assert price_value == 58.29, f"Итоговая сумма должна быть 58.29, "
    "а получена {price_value}"

    driver.quit()
