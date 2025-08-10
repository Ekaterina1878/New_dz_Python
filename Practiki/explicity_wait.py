from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("http://www.uitestingplayground.com/progressbar")

waiter = WebDriverWait(driver, 50, 0.2)
#в переменной находится экземпляр с параметрами: 
# 1 параметр - наш драйвер, 2 параметр - 40 секунд на ожидание
#запуск индикатора прогресса:нажали на кнопку старт
driver.find_element(By.CSS_SELECTOR, "#startButton").click()
#ожидание выполнения условий:
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)
#омтановили индикатор прогресса:нажали на кнопку стоп
driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print( driver.find_element(By.CSS_SELECTOR, "#result").text )
# найди текст элемента и выведи его в терминал
driver.quit()
