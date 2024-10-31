import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navigate_to_cart_page(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    assert "cart.html" in driver.current_url
    
def test_navigate_to_product_detail_page(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.ID, "item_4_img_link").click()
    time.sleep(3)
    assert "id=4" in driver.current_url

def test_navigate_to_checkout_page(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)
    assert "checkout" in driver.current_url