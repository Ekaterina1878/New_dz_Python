from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://ya.ru")
# browser.get("https://rzd.ru")
sleep(3)

url = browser.current_url
print(url)

browser.quit()
