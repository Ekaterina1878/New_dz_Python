import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-"
        "java/slow-calculator.html")

    # Очистка поля ввода и введение числа 45
    input_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    input_delay.clear()
    input_delay.send_keys("45")
    # Нажатие на кнопки
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание и проверка результа
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen")))

    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"

