import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Go to Home Page
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

# Step 3: Go to Registration page from My Account
my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
my_account.click()

register = driver.find_element(By.CSS_SELECTOR, ".list-inline  ul > li:nth-of-type(1) > a")
register.click()
time.sleep(2)

first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
first_name.send_keys("Smith")

last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
last_name.send_keys("Test")

email = driver.find_element(By.CSS_SELECTOR, "#input-email")
email.send_keys(fake.email())

telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
telephone.send_keys("1234567889")

password = driver.find_element(By.CSS_SELECTOR, "#input-password")
password.send_keys("123456")

confirm_password = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
confirm_password.send_keys("123456")

privacy_policy = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
privacy_policy.click()

continue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
continue_button.click()
time.sleep(4)

#  verify that account created successfully
expected_success_text = "Your Account Has Been Created!"

actual_success_element = driver.find_element(By.CSS_SELECTOR, "#content h1")
actual_success_text = actual_success_element.text

if expected_success_text == actual_success_text:
    print("Account created successfully.Test Passed")
else:
    print("Account create failed.Test Failed")
