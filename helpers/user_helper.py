from config.config_manager import ConfigManager
from helpers.random_helper import get_n_random_alphanumericals


class UserHelper:
    user_config = ConfigManager.get_config()["user"]

    @classmethod
    def get_valid_user(cls) -> dict:
        login_data = {"email": cls.user_config["email"], "password": cls.user_config["password"]}
        return login_data

    @classmethod
    def get_user_with_invalid_email(cls) -> dict:
        email = f'{get_n_random_alphanumericals()}@{get_n_random_alphanumericals(5)}.{get_n_random_alphanumericals(3)}'
        login_data = cls.get_valid_user()
        login_data["email"] = email
        return login_data

    @classmethod
    def get_user_with_email_not_email(cls) -> dict:
        email = get_n_random_alphanumericals()
        login_data = cls.get_valid_user()
        login_data["email"] = email
        return login_data

    @classmethod
    def get_user_with_invalid_password(cls) -> dict:
        password = get_n_random_alphanumericals()
        login_data = cls.get_valid_user()
        login_data["password"] = password
        return login_data

    @classmethod
    def get_user_with_invalid_email_and_password(cls) -> dict:
        email = f'{get_n_random_alphanumericals()}@{get_n_random_alphanumericals(5)}.{get_n_random_alphanumericals(3)}'
        password = get_n_random_alphanumericals()
        login_data = {"email": email, "password": password}
        return login_data
