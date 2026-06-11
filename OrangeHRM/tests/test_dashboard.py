from OrangeHRM.utils.logger import get_logger
from OrangeHRM.utils.conftest import driver_setup
from OrangeHRM.pages.login import LoginPage
from OrangeHRM.pages.dashboard import Dashboard

log = get_logger()

def test_dashboard(driver_setup):
    driver = driver_setup

    log.info("Logging in ...!")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    log.info("Opening dashboard ...!")
    dashboard = Dashboard(driver)
    dashboard.apply_leave_click()
    log.info("Apply leave clicked successfully")


