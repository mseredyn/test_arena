from time import sleep

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config.config_manager import ConfigManager
from helpers.user_helper import UserHelper
from page.login_page import LoginPage


@pytest.fixture(scope="function")
def webdriver_factory():
    class DriverFactory:
        drivers = []

        @staticmethod
        def get():
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument('disable-infobars')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

            driver.get(ConfigManager.get_config()["url"])
            return driver

    yield DriverFactory()

    for driver in DriverFactory.drivers:
        driver.close()


@pytest.fixture(scope="function")
def webdriver_logged_in_factory(webdriver_factory):
    class DriverLoggedInFactory:
        @staticmethod
        def get():
            driver = webdriver_factory.get()
            page = LoginPage(driver)
            user = UserHelper.get_valid_user()
            page.fill_email_and_password(user["email"], user["password"])
            page.click_login_button()

            return driver

    return DriverLoggedInFactory()
