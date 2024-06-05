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