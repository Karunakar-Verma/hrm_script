import pytest
from selenium import webdriver


@pytest.fixture
def driver_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

