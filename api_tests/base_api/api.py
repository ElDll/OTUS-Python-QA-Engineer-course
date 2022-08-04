from jsonschema import validate
from ..base_api.requests import Client
from ..base_api.models import ResponseModel


class Request:
    def __init__(self, url, path):
        self.url = url
        self.client = Client()
        self.path = path

    def dog_request(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path}")
        validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, response=response.json())

    def open_brewery_request(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path}")
        validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, response=response.json())

    def json_placeholder_request(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path}")
        validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, response=response.json())

