import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Login Page URL Open
driver.get("https://www.saucedemo.com/")

# Step 3: Enter Email/Username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
time.sleep(2)

# Step 4: Enter Password
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)

# Step 5: Click Login Button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(5)