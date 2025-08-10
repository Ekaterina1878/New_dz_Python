from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://ya.ru")
# txt = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').text#сбор инфо
# #об элементе
# print(txt)#вывод инфо в терминал

# tag = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').tag_name #сбор инфо о теге
# print(tag)

# id = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').id #сбор инфо об id
# print(id)

# href= driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').get_attribute("href") #сбор инфо по атрибуту
# print(href)

# color = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("color") #сбор инфо по св-ву css
# print(color)

# driver.get("http://uitestingplayground.com/visibility")

# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed) #вывод статуса видимости Opacity 0

# driver.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide
# # Opacity 0 окажется скрытой
# sleep(3)

# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed() #еще раз
# #проверяем видимость Opacity 0
# print(is_displayed)
# sleep(3)

# driver.get("https://demoqa.com/radio-button")
# sleep(10)

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)# выводим в косносль кнопка взаимодействует True

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
# print(is_enabled)# выводим в косносль кнопка не доступна False

driver.get("https://the-internet.herokuapp.com/checkboxes")
sleep(5)
is_selected = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]").is_selected()
print(is_selected)

driver.quit()
