import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Go to Home Page
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

# Step 3: Go to Registration page from My Account
my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
my_account.click()

login = driver.find_element(By.CSS_SELECTOR, ".list-inline  ul > li:nth-of-type(2) > a")
login.click()
time.sleep(2)

# Step 4: Login page
email = driver.find_element(By.CSS_SELECTOR, "input#input-email")
email.send_keys("mail123@gmail.com")

password = driver.find_element(By.CSS_SELECTOR,"#input-password")
password.send_keys("123456")

login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
login_button.click()
time.sleep(5)

# verify login success or not
expected_account_url = "https://tutorialsninja.com/demo/index.php?route=account/account"

actual_account_url = driver.current_url

if expected_account_url == actual_account_url:
    print("Login Successful.Test Passed")
else:
    print("Login failed.Test Failed")
