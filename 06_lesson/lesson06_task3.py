from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 120).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)

WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))

img = driver.find_element(By.CSS_SELECTOR, "#award")
img_src = img.get_attribute("src")
print(img_src)

driver.quit()
