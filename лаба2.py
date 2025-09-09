from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

try:
    driver.get("https://www.saucedemo.com/")
    
    time.sleep(2)
    
    username_field = driver.find_element(By.NAME, "user-name")
    username_field.send_keys("standard_user")
    
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.NAME, "login-button")
    login_button.click()

    filter = driver.find_element(By.CLASS_NAME, "product_sort_container")
    filter.click()
    time.sleep(1)
    option=driver.find_element(By.XPATH, "//option[@value='hilo']")
    option.click()
    time.sleep(1)
    button = driver.find_element(By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)")
    button.click()
    time.sleep(3)
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
    time.sleep(2)
    remove = driver.find_element(By.NAME, "remove-test.allthethings()-t-shirt-(red)")
    remove.click()
    time.sleep(2)
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    driver.quit()
