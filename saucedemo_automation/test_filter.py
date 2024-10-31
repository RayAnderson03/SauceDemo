import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_filter_from_A_to_Z(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    filter_element = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    filter_element.select_by_value("az")
    time.sleep(2)  
    product_names = [element.text for element in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert product_names == sorted(product_names)
    
def test_filter_from_Z_to_A(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    filter_element = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    filter_element.select_by_value("za")
    time.sleep(2)  
    product_names = [element.text for element in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert product_names == sorted(product_names, reverse=True)

def test_filter_from_low_to_high(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    filter_element = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    filter_element.select_by_value("lohi")
    time.sleep(2)  
    product_prices = [float(element.text.replace('$', '')) for element in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert product_prices == sorted(product_prices)

def test_filter_from_high_to_low(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    filter_element = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    filter_element.select_by_value("hilo")
    time.sleep(2)  
    product_prices = [float(element.text.replace('$', '')) for element in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert product_prices == sorted(product_prices, reverse=True)
