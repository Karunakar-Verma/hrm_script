from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    btn = (By.XPATH, "//button[@type='submit']")

    def __init__(self,driver_setup):
        self.driver = driver_setup
        self.wait = WebDriverWait(self.driver, 20)

    def enter_username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)

    def enter_password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)


    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.btn)).click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()







