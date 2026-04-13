import requests
from config.settings import BASE_URL, HEADERS, TIMEOUT

import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def get(self, endpoint: str):
        return self.session.get(self.base_url + endpoint)

    def post(self, endpoint: str, json: dict):
        return self.session.post(self.base_url + endpoint, json=json)

    def put(self, endpoint: str, json: dict):
        return self.session.put(self.base_url + endpoint, json=json)
    def delete(self, endpoint: str):
        return self.session.delete(self.base_url + endpoint)