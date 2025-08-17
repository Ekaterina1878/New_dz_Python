import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\angel\OneDrive\Desktop\
        msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-" 
               "java/data-types.html")

    # Ожидание и заполнение формы
    first_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "[name='first-name']")))
    first_name.send_keys("Иван")

    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    # Нажатие на кнопку Submit
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']").click()

    # Ожидание, пока поле Zipcode станет доступным
    zip_code_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#zip-code")))

    # Проверка подсветки поля Zipcode красным
    zip_code_color = zip_code_field.value_of_css_property("background-color")
    assert zip_code_color == "rgba(248, 215, "
    " 218, 1)", "Zip code field is not highlighted in red"

    # Проверка подсветки остальных полей зеленым
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city",
              "country", "job-position", "company"]
    for field_name in fields:
        element_color = driver.find_element(
            By.ID, field_name).value_of_css_property("background-color")
    assert element_color == "rgba(209, 231, "
    " 221, 1)", "First name field is not highlighted in green"
