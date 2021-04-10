import json
import os
import yaml
import requests
from requests import HTTPError


class MainInstance:
    """
    Loading configuration from YML file
    """

    def get_config(self):
        with open(os.path.join(os.getcwd(), './config.yml'), mode='r') as context:
            config = yaml.safe_load(context)

            self.api = config["api"]["url"]

            self.api_endpoint = config["api"]["endpoint"]
            self.api_payload = config["api"]['payload']

            self.auth_endpoint = config["auth"]["endpoint"]
            self.auth_payload = config["auth"]['payload']
        return config

    """
    Authorization
    """

    def auth(self):
        try:
            headers = {'content-type': 'application/json'}
            url = f'{self.api}{self.auth_endpoint}'
            data = json.dumps(self.auth_payload)

            result = requests.post(url, data=data, headers=headers)
            data = result.json()

            access_token = data['access_token']
            self.get_data(access_token)

        except HTTPError:
            print('Error auth')

    """
    Get data from API
    """

    def get_data(self, access_token):
        try:
            url = f'{self.api}{self.api_endpoint}'
            headers = {'Authorization': f'JWT {access_token}'}
            result = requests.get(url, params=self.api_payload, headers=headers)
            data = result.json()

            self.save_as(data)
        except HTTPError:
            pass
        pass

    """
    Save data in
        ./<payload_date>/data.json
    """

    def save_as(self, data):
        dir_name = self.api_payload["date"]
        filename = "data"

        if not os.path.exists(f"./{dir_name}"):
            os.makedirs(dir_name)

        with open(f'./{dir_name}/{filename}.json', 'w') as file:
            json.dump(data, file)

    """
    Initializing
    """
    def __init__(self):
        self.get_config() # get configuration form YML file
        self.auth() # authorization


if __name__ == '__main__':
    MainInstance()
    pass
