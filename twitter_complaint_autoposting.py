### if my internet speed is less than 100.01, then it will automatically 
### post it on my twitter acc.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

def data_speed_test():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.speedtest.net/")

    time.sleep(5)
    continue_btn = driver.find_element(By.ID, value="onetrust-accept-btn-handler")
    continue_btn.click()

    go_btn = driver.find_element(By.CLASS_NAME, value="start-text")
    go_btn.click()

    global up, down
    time.sleep(40)
    up_str = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    down_str = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    up = float(up_str)
    down = float(down_str) 
    
    

def tweeting():
    global up,down
    USER_NAME = "SeetaA376967"
    PASSWORD = "siri2323"

    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://twitter.com/login")

    time.sleep(3)
    login_name = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    login_name.send_keys(USER_NAME)
    next_btn = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
    next_btn.click()

    time.sleep(2)
    login_password = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    login_password.send_keys(PASSWORD)
    login_btn = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
    login_btn.click()

    time.sleep(10)
    complaint = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    complaint.send_keys(f"The internet speed is not as fast as mentioned. Current speed: {up},  {down}")
    post_btn = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
    post_btn.click()

    print("Tweet posted!")

data_speed_test()

if up < 100.01 and down < 100.01:
    tweeting()
