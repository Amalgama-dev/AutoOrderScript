from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://mafia.ua/kiev/product/kombo-menyu-gamburger-13882"
driver = webdriver.Chrome(executable_path='/home/amalgama/AutoOrderScript/chromedriver/chromedriver')



try:
    driver.get(url=url)
    time.sleep(3)
    html = driver.find_element(By.XPATH, '/html')
    for i in range(13):
        html.send_keys(Keys.DOWN)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div/div[3]/div[3]/div[1]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/header/div[2]/div[2]/div[3]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="popup-cart"]/div/div[3]/a').click()
    time.sleep(3)
    htmlcart = driver.find_element(By.XPATH, '/html')
    for i in range(15):
        htmlcart.send_keys(Keys.DOWN)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/a').click()
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
