from OrangeHRM.pages.login import LoginPage
from OrangeHRM.utils.conftest import driver_setup
from OrangeHRM.utils.logger import get_logger

logger = get_logger()

def test_login(driver_setup):
    driver = driver_setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    logger.info("Entering username..!")
    login.enter_username("Admin")
    logger.info("Entering password..!")
    login.enter_password("admin123")
    logger.info("Clicked submit..!")
    login.click_submit()

    assert "dashboard" in driver.current_url.lower()
    logger.info("Assertion passed..!")
    driver.quit()

def test_login_fail(driver_setup):
    driver = driver_setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin12345")
    login.click_submit()

    assert "dashboard" not  in driver.current_url.lower()
    driver.quit()


