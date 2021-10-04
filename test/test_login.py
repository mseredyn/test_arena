import pytest

from helpers.user_helper import UserHelper
from page.dashboard_page import DashboardPage
from page.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, webdriver_factory):
        driver = webdriver_factory.get()
        page = LoginPage(driver)
        user = UserHelper.get_valid_user()
        page.fill_email_and_password(user["email"], user["password"])
        page.click_login_button()
        DashboardPage(driver)

    def test_email_not_email_login(self, webdriver_factory):
        driver = webdriver_factory.get()
        page = LoginPage(driver)
        user = UserHelper.get_user_with_email_not_email()
        page.fill_email_and_password(user["email"], user["password"])
        page.click_login_button()
        page.assert_invalid_format_error_shown()
        page.assert_invalid_email_or_password_error_shown()

    @pytest.mark.parametrize("user_candidate",
                             [UserHelper.get_user_with_invalid_email(), UserHelper.get_user_with_invalid_password(),
                              UserHelper.get_user_with_invalid_email_and_password()])
    def test_invalid_user_data_login(self, webdriver_factory, user_candidate):
        driver = webdriver_factory.get()
        page = LoginPage(driver)
        page.fill_email_and_password(user_candidate["email"], user_candidate["password"])
        page.click_login_button()
        page.assert_invalid_email_or_password_error_shown()
