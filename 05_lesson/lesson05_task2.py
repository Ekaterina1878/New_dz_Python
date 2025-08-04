from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

sleep(5)
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

sleep(10)
quit()
