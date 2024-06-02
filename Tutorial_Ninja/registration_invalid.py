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

# registration page
first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
first_name.send_keys("")

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

#  verify error message for first name
expected_error_text = "First Name must be between 1 and 32 characters!"

actual_error_element = driver.find_element(By.CSS_SELECTOR, ".text-danger")
actual_error_text = actual_error_element.text

if expected_error_text == actual_error_text:
    print("Error text for first name match.Test Passed")
else:
    print("Error text for first name mismatch.Test Failed")

