import requests
import json


class KrakenAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.octopus.energy"
        self.session = requests.Session()
        self.session.auth = (f'{self.api_key}:', "")

    def _make_request(self, url):
        response = self.session.get(url)
        if response.status_code != 200:
            print("Error: ", response.status_code)
            print(response.content)
            return None
        response_json = json.loads(response.content)
        return response_json

    def get_meter_point(self, mpan):
        url = f"{self.base_url}/v1/electricity-meter-points/{mpan}/"
        return self._make_request(url)

    def get_meter_point_consumption(self, mpan, serial):
        url = f"{self.base_url}/v1/electricity-meter-points/{mpan}/meters/{serial}/consumption/"
        return self._make_request(url)

    def get_gas_meter_point_consumption(self, mpan, serial):
        url = f"{self.base_url}/v1/gas-meter-points/{mpan}/meters/{serial}/consumption/"
        return self._make_request(url)


    def get_products(self):
        url = f"{self.base_url}/v1/products/"
        return self._make_request(url)

    def close(self):
        self.session.close()
