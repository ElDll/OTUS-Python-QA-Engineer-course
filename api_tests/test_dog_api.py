from .base_api.api import Request
from .schemas.dog_schema import dog_schema
import pytest


base_url = "https://dog.ceo/api/breed"


def test_random_image():
    response = Request(url=base_url + "s", path='/image/random').dog_request(dog_schema(message_type={"type": "string"}))
    assert response.status == 200
    assert response.response.get('message')
    assert response.response.get('status') == "success"


def test_incorrect_random_image():
    response = Request(url=base_url + "s", path='/image/random1').dog_request(dog_schema(message_type={"type": "string"}))
    assert response.status == 404
    assert response.response.get('message')
    assert response.response.get('status') == "error"


@pytest.mark.parametrize('path, status, schema, code',
                         [('/hound/images', 'success', dog_schema(message_type={"type": "array"}), 200),
                          ('/hound/images/random', 'success', dog_schema(message_type={"type": "string"}), 200),
                          ('/hound/images/random/3', 'success', dog_schema(message_type={"type": "array"}), 200),
                          ('/dvornyaga/images', 'error', dog_schema(message_type={"type": "string"}), 404)]
                         )
def test_by_breed_request(path, status, schema, code):
    response = Request(url=base_url, path=path).dog_request(schema=schema)
    assert response.status == code
    assert response.response.get('message')
    assert response.response.get('status') == status


@pytest.mark.parametrize('path, status, schema, code',
                         [('/hound/list', 'success', dog_schema(message_type={"type": "array"}), 200),
                          ('/hound/afghan/images', 'success', dog_schema(message_type={"type": "array"}), 200),
                          ('/hound/afghan/images/random', 'success', dog_schema(message_type={"type": "string"}), 200),
                          ('/hound/afghan/images/random/3', 'success', dog_schema(message_type={"type": "array"}), 200),
                          ('/hound/dvornyaga', 'error', dog_schema(message_type={"type": "string"}), 404)]
                         )
def test_by_sub_breed_request(path, status, schema, code):
    response = Request(url=base_url, path=path).dog_request(schema=schema)
    assert response.status == code
    assert response.response.get('message')
    assert response.response.get('status') == status


def test_all_breeds_request():
    response = Request(url=base_url + "s", path='/list/all').dog_request(dog_schema(message_type={"type": "object"}))
    assert response.status == 200
    assert response.response.get('message')
    assert response.response.get('status') == "success"

