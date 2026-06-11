from selenium.webdriver.common.by import By
from OrangeHRM.utils.conftest import driver_setup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:

    apply_leave_btn = (By.XPATH, "//button[@title='Apply Leave']")

    def __init__(self,driver_setup):
        self.driver = driver_setup
        self.wait = WebDriverWait(self.driver,20)


    def apply_leave_click(self):
        self.wait.until(EC.visibility_of_element_located(self.apply_leave_btn)).click()



