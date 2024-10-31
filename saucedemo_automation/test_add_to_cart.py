import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"
    
def test_remove_product_from_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(3)
    cart_badge_element = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge_element) == 0
    
def test_verify_product_in_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    assert "cart.html" in driver.current_url
    
def test_add_same_product_multiple_times(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "cart_quantity").send_keys("2")
    time.sleep(3)
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "2"