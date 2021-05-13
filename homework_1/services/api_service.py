import json
import os

from requests import HTTPError
import requests


class ApiService:
    conf = None
    access_token = None

    def __init__(self, conf):
        self.conf = conf
        self.access_token = self.get_access_token()

    """
    Authorization. Get access token
    """

    def get_access_token(self):
        try:
            headers = {'content-type': 'application/json'}
            url = f'{self.conf["api"]["url"]}{self.conf["auth"]["endpoint"]}'

            payload = json.dumps(self.conf["auth"]["payload"])
            response = requests.post(url, data=payload, headers=headers)

            if response.status_code != 200:
                raise Exception("Auth Fail")

            try:
                return response.json()['access_token']
            except Exception:
                return ValueError('Access token was not received')

        except HTTPError:
            print('Error auth')


    """
    Get data from API
    """

    def get_data(self, date):
        try:
            url = f'{self.conf["api"]["url"]}{self.conf["api"]["endpoint"]}'
            headers = {'Authorization': f'JWT {self.access_token}'}
            response = requests.get(url, params={"date": date}, headers=headers)

            if response.status_code != 200:
                raise Exception("Auth Fail")

            data = response.json()

            self.save_as(data, date)
        except HTTPError:
            pass
        pass

    """
    Save data in
        ./data/<payload_date>/data.json
    """

    def save_as(self, data, dir_name):
        if not os.path.exists(f"./data/{dir_name}"):
            os.makedirs(f"./data/{dir_name}")

        with open(f'./data/{dir_name}/data.json', 'w') as file:
            json.dump(data, file)