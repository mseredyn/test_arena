import yaml
from yaml.loader import SafeLoader

from helpers.path_helper import PROJECT_ROOT


class ConfigManager(object):
    config = None

    @classmethod
    def load_config(cls):
        with open(f'{PROJECT_ROOT}/config/config.yml') as f:
            cls.config = yaml.load(f, Loader=SafeLoader)

    @classmethod
    def get_config(cls) -> dict:
        if not cls.config:
            cls.load_config()
        return cls.config
