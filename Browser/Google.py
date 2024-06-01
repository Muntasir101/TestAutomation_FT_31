import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Login Page URL Open
driver.get("https://www.google.com/")
time.sleep(5)

search = driver.find_element(By.NAME, "q")
search.send_keys("Bangladesh")
time.sleep(4)

search_button = driver.find_element(By.NAME, "btnK")
search_button.click()
time.sleep(3)