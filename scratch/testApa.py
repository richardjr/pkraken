# DOCS: https://developer.octopus.energy/docs/api/

import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def test_api(key):

    # Start a session because its an authenticated API :/
    session = requests.Session()
    # Note the added : after the key
    session.auth = (key+':', "")


    base_url = "https://api.octopus.energy"
    endpoint = "/v1/products/"

    url = base_url + endpoint
    response = session.get(url)

    if response.status_code != 200:
        print("Error: ", response.status_code)
        print(response.content)
        return
    response_json = json.loads(response.content)
    for result in response_json['results']:
        print(result['display_name'])

test_api(os.getenv("API_KEY"))