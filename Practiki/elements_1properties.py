from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# #записываем верхнюю html-ветку в переменную div
# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# #через div идем по ветке до элемента с тегом a
# a = div.find_element(By.CSS_SELECTOR, "a")
# #запрашиваем ссылку из элемента с тегом a
# print(a.get_attribute("href"))

# driver.quit()

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# sleep(3)
# #ищем все элементы по тегу div и записываем в переменную divs:
# divs = driver.find_elements(By.CSS_SELECTOR, "div")
# #запрашиваем длину списка
# l = len(divs)
# print(l)

# driver.quit()

driver.get("https://the-internet.herokuapp.com/checkboxes")
sleep(3)
#ищем все элементы по тегу div и записываем в переменную divs:
divs = driver.find_elements(By.CSS_SELECTOR, "div")
#ищем элемент по индексу
#в переменную div помещаем элемент с индексом = 6 из списка divs:
div = divs[6]
#запрашиваем атрибуты и помещаем в переменную css_class:
css_class = div.get_attribute("class")
#выводим в терминал:
print(css_class)


