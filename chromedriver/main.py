from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from settings_data import name, number, street, house, entrance, apartment
import time

url = "https://mafia.ua/kiev/product/kombo-menyu-gamburger-13882"
driver = webdriver.Chrome(executable_path='./driver/chromedriver')



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
    name_input.send_keys(name)
    number_input = driver.find_element(By.XPATH, '//*[@id="checkout"]/div/div[4]/form/div[2]/input')
    number_input.send_keys(number) 
    street_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[2]/input')
    street_input.send_keys(street)
    time.sleep(1)
    street_input.send_keys(Keys.DOWN)
    street_input.send_keys(Keys.ENTER)
    house_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[3]/input')
    house_input.send_keys(house)
    entrance_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[4]/input')
    entrance_input.send_keys(entrance)
    apartment_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[3]/div/div[5]/input')
    apartment_input.send_keys(apartment)
    htmlcart = driver.find_element(By.XPATH, '/html')
    for i in range(10):
        htmlcart.send_keys(Keys.DOWN)
    time.sleep(2)
    call_input = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[4]/form/div[10]/label/div').click()
    confirm = driver.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[5]/a').click()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
