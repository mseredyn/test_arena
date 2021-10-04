from page.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = "//input[@name='email']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//input[@name='login']"
    PAGE_SUB_URL = "zaloguj"
    # EMAIL_INVALID_FORMAT_ERROR = "//div[text()='Invalid email format. Please enter your email again.']"
    # EMAIL_OR_PASSWORD_INCORRECT_ERROR = "//div[text()='Your email and/or password is incorrect.']"
    EMAIL_OR_PASSWORD_INCORRECT_ERROR = "//div[text()='Adres e-mail i/lub hasło są niepoprawne.']"
    EMAIL_INVALID_FORMAT_ERROR = "//div[text()='Nieprawidłowy format adresu e-mail. Wprowadź adres ponownie.']"

    def __init__(self, driver):
        super().__init__(driver)
        self.assert_sub_page_url(self.PAGE_SUB_URL)

    def fill_email(self, email):
        self.fill_with_value_by_xpath(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.fill_with_value_by_xpath(self.PASSWORD_INPUT, password)

    def fill_email_and_password(self, email, password):
        self.fill_email(email)
        self.fill_password(password)

    def click_login_button(self):
        self.click_by_xpath(self.LOGIN_BUTTON)

    def assert_invalid_format_error_shown(self):
        self.find_by_xpath(self.EMAIL_INVALID_FORMAT_ERROR)

    def assert_invalid_email_or_password_error_shown(self):
        self.find_by_xpath(self.EMAIL_OR_PASSWORD_INCORRECT_ERROR)
