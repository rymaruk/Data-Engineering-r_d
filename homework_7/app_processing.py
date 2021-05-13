import json
import os
import yaml
from services.api_service import ApiService


class AppProcessing:
    """
    Initialize main application
    """

    def app_main(self, config, date):
        api = ApiService(config)
        api.get_data(date)

    """
    Loading configuration from YML file
    """

    def get_config(self):
        try:
            with open(os.path.join(os.getcwd(), './config.yml'), mode='r') as context:
                return yaml.safe_load(context)
        except Exception as exc:
            raise Exception("Parse config error".format(exc))

    """
    Initializing
    """

    def run(self):
        config = self.get_config()  # get configuration form YML file
        self.app_main(config, "2021-01-05")
