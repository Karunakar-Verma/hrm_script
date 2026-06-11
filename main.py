import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_orangehrm_login():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    assert "Dashboard" in driver.page_source
