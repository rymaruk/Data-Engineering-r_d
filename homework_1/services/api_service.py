import json
import os

from requests import HTTPError
import requests


class ApiService:
    conf = None

    def __init__(self, conf):
        self.conf = conf


    """
    Authorization. Get access token
    """

    def get_access_token(self):
        try:
            headers = {'content-type': 'application/json'}
            url = f'{self.conf["api"]}{self.conf["endpoint"]}'

            response = requests.post(url, data=json.dumps(self.conf["auth"]["payload"]), headers=headers)

            if response.status_code != 200:
                raise Exception("Auth Fail")
            try:
                return response.json()['access_token']
            except Exception:
                return ValueError('Access token was not received')

        except HTTPError:
            print('Error auth')

    """
    Save data in
        ./data/<payload_date>/data.json
    """

    def save_as(self, data, dir_name):
        if not os.path.exists(f"./data/{dir_name}"):
            os.makedirs(f"./data/{dir_name}")

        with open(f'./data/{dir_name}/data.json', 'w') as file:
            json.dump(data, file)