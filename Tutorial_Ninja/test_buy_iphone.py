import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_launch_browser(driver):
    assert driver is not None


def test_open_home_page(driver):
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)


def test_go_to_myAccount(driver):
    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()
    time.sleep(2)


def test_click_login_in_myAccount(driver):
    login = driver.find_element(By.CSS_SELECTOR, ".list-inline  ul > li:nth-of-type(2) > a")
    login.click()
    time.sleep(2)


def test_enter_email(driver):
    email = driver.find_element(By.CSS_SELECTOR, "input#input-email")
    email.send_keys("mail123@gmail.com")
    time.sleep(2)


def test_enter_password(driver):
    password = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password.send_keys("123456")
    time.sleep(2)


def test_click_login_button(driver):
    login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
    login_button.click()
    time.sleep(5)


def test_go_to_home_page(driver):
    home_page_link = driver.find_element(By.LINK_TEXT, "Qafox.com")
    home_page_link.click()
    time.sleep(2)


def test_click_iPhone(driver):
    iphone = driver.find_element(By.CSS_SELECTOR, ".row > div:nth-of-type(2) h4 > a")
    iphone.click()
    time.sleep(2)


def test_click_add_to_cart(driver):
    add_to_cart = driver.find_element(By.CSS_SELECTOR, "button#button-cart")
    add_to_cart.click()


def test_success_message(driver):
    expected_success_text = """Success: You have added iPhone to your shopping cart!
    ×"""

    actual_success_element = driver.find_element(By.CLASS_NAME, 'alert-success')
    actual_success_text = actual_success_element.text

    if expected_success_text == actual_success_text:
        print("Item added successfully.Test Passed")
    else:
        print("Item add failed.Test Failed")


def test_go_to_checkout_page(driver):
    checkout = driver.find_element(By.CSS_SELECTOR, "a[title='Checkout'] > .hidden-md.hidden-sm.hidden-xs")
    checkout.click()
    time.sleep(2)


def test_click_final_checkout(driver):
    final_checkout = driver.find_element(By.CSS_SELECTOR, "#content div:nth-child(8) .btn-primary")
    final_checkout.click()
