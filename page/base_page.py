from hamcrest import assert_that, equal_to, ends_with, starts_with
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config_manager import ConfigManager


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_by_xpath(self, xpath):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath)

    def click_by_xpath(self, xpath):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.find_by_xpath(xpath).click()

    def fill_with_value_by_xpath(self, xpath, value_to_fill):
        self.find_by_xpath(xpath).send_keys(value_to_fill)

    def assert_sub_page_url(self, url_expected):
        actual_url = self.driver.current_url
        base_url = ConfigManager.get_config()["url"]
        assert_that(actual_url, starts_with(base_url))
        assert_that(actual_url, ends_with(url_expected))
