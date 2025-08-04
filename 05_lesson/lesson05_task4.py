from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")
sleep(3)

input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
input_username.send_keys("tomsmith")
sleep(3)

input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
input_password.send_keys("SuperSecretPassword!")
sleep(3)

button_login = driver.find_element(By.CSS_SELECTOR, "i.fa-sign-in").click()
sleep(3)

text = driver.find_element(By.CSS_SELECTOR, "div#flash").text
print(text)

driver.quit()
