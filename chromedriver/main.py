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
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/header/div[2]/div[2]/div[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="popup-cart"]/div/div[3]/a').click()
    time.sleep(2)
    htmlcart = driver.find_element(By.XPATH, '/html')
    for i in range(15):
        htmlcart.send_keys(Keys.DOWN)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/a').click()
    time.sleep(2)
    name_input = driver.find_element(By.XPATH, '//*[@id="checkout"]/div/div[4]/form/div[1]/input')
    name_input.send_keys('name')
    time.sleep(3)
    namber_input = driver.find_element(By.XPATH, '//*[@id="checkout"]/div/div[4]/form/div[2]/input')
    namber_input.send_keys('0666684037')
    time.sleep(3)
    street_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[2]/input')
    street_input.send_keys('Победы')
    house_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[3]/input')
    house_input.send_keys('51')
    entrance_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[4]/input')
    entrance_input.send_keys('1')
    apartment_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[5]/input')
    apartment_input.send_keys('1')
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
