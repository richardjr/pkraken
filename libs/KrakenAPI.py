import requests
import json


class KrakenAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.octopus.energy"
        self.session = requests.Session()
        self.session.auth = (f'{self.api_key}:', "")

    def get_meter_point(self, mpan):
        url = f"{self.base_url}/v1/electricity-meter-points/{mpan}/"
        response = self.session.get(url)
        if response.status_code != 200:
            print("Error: ", response.status_code)
            print(response.content)
            return None
        response_json = json.loads(response.content)
        return response_json

    def get_meter_point_consumption(self, mpan, serial):
        url = f"{self.base_url}/v1/electricity-meter-points/{mpan}/meters/{serial}/consumption/"
        response = self.session.get(url)
        if response.status_code != 200:
            print("Error: ", response.status_code)
            print(response.content)
            return None
        response_json = json.loads(response.content)
        return response_json

    def get_products(self):
        url = f"{self.base_url}/v1/products/"
        response = self.session.get(url)
        if response.status_code != 200:
            print("Error: ", response.status_code)
            print(response.content)
            return None
        response_json = json.loads(response.content)
        return response_json

    def close(self):
        self.session.close()
