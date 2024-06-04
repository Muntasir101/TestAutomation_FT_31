import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Step 1: Launch Browser
driver = webdriver.Firefox()
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

password = driver.find_element(By.CSS_SELECTOR, "#input-password")
password.send_keys("123456")

login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
login_button.click()
time.sleep(5)

home_page_link = driver.find_element(By.LINK_TEXT, "Qafox.com")
home_page_link.click()
time.sleep(2)

apple_cinema = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) h4 > a")
apple_cinema.click()
time.sleep(2)

# Options
small = driver.find_element(By.CSS_SELECTOR, ".radio [type]")
small.click()
time.sleep(3)

checkbox3 = driver.find_element(By.CSS_SELECTOR, "#product .checkbox:nth-of-type(1) [type]")
checkbox3.click()
time.sleep(3)

checkbox4 = driver.find_element(By.CSS_SELECTOR, "#product .checkbox:nth-of-type(2) [type]")
checkbox4.click()
time.sleep(3)

# color select
color_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='option[217]']")
color_options = Select(color_dropdown)
color_options.select_by_value("3")
time.sleep(3)

# textarea
textarea = driver.find_element(By.CSS_SELECTOR, "textarea[name='option[209]']")
textarea.clear()
textarea.send_keys("Test Test from Selenium")
time.sleep(3)

# date
date = driver.find_element(By.CSS_SELECTOR, ".date .form-control")
date.clear()
date.send_keys("2011-02-22")
time.sleep(3)

# time
times = driver.find_element(By.CSS_SELECTOR, ".time .form-control")
times.clear()
times.send_keys("10:10")
time.sleep(3)

# date time
date_time = driver.find_element(By.CSS_SELECTOR, ".datetime .form-control")
date_time.clear()
date_time.send_keys("2011-02-22 10:10")
time.sleep(3)

file_upload_button = driver.find_element(By.ID, "button-upload222")
file_upload_button.click()
file_upload_button.send_keys("C:\\Users\\Asus\\Desktop\\1.jpg")
time.sleep(5)

# success Alert
driver.switch_to.alert.accept()

# add to cart
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button#button-cart")
add_to_cart_button.click()
time.sleep(10)
