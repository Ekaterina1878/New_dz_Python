from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

my_cookie = { #придумываем название перемнной и добавляем объект
    'name': 'cookie_policy', #ключ
	'value': '1'}  #значение

browser.get("https://labirint.ru")
browser.add_cookie(my_cookie) #добавляем куки

# cookies = browser.get_cookies() #переменная в кот. соберутся все куки
# print(cookies) #выводим данные в консоль

cookie = browser.get_cookie('PHPSESSID') #переменная с именем из собранных куки
print(cookie) #выводим данные этой куки в консоль

# browser.refresh() #обновляем страницу
# browser.delete_all_cookies() #чистим куки, удаляем все куки

browser.refresh()

sleep(10)

browser.quit()
