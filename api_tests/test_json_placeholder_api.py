from .base_api.api import Request
from .schemas.json_placeholder_schema import json_placeholder_schema
import pytest


base_url = "https://jsonplaceholder.typicode.com"


def test_posts_request():
    response = Request(url=base_url, path='/posts/1').json_placeholder_request(
        schema=json_placeholder_schema(schema_type='posts'))
    assert response.status == 200
    assert response.response.get('userId') == 1
    assert response.response.get('id') == 1
    assert response.response.get('title') == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'


def test_comments_request():
    response = Request(url=base_url, path='/comments/1').json_placeholder_request(
        schema=json_placeholder_schema(schema_type='comments'))
    assert response.status == 200
    assert response.response.get('postId') == 1
    assert response.response.get('id') == 1
    assert response.response.get('name') == 'id labore ex et quam laborum'
    assert response.response.get('email') == 'Eliseo@gardner.biz'


@pytest.mark.parametrize('position, schema, userId, id, title, status_code',
                         [('1', 'albums', 1, 1, 'quidem molestiae enim', 200),
                          ('100', 'albums', 10, 100, 'enim repellat iste', 200),
                          ('101', 'empty', None, None, None, 404)]
                         )
def test_albums_request(position, schema, userId, id, title, status_code):
    response = Request(url=base_url, path=f'/albums/{position}').json_placeholder_request(
        schema=json_placeholder_schema(schema_type=schema))
    assert response.status == status_code
    assert response.response.get('userId') == userId
    assert response.response.get('id') == id
    assert response.response.get('title') == title


@pytest.mark.parametrize('position, schema, albumId, id, title, url, thumbnailUrl, status_code',
                         [('1', 'photos', 1, 1, 'accusamus beatae ad facilis cum similique qui sunt',
                           'https://via.placeholder.com/600/92c952', 'https://via.placeholder.com/150/92c952', 200),
                          ('5000', 'photos', 100, 5000, 'error quasi sunt cupiditate voluptate ea odit beatae',
                           'https://via.placeholder.com/600/6dd9cb', 'https://via.placeholder.com/150/6dd9cb', 200),
                          ('5001', 'empty', None, None, None, None, None, 404)]
                         )
def test_photos_request(position, schema, albumId, id, title, url, thumbnailUrl, status_code):
    response = Request(url=base_url, path=f'/photos/{position}').json_placeholder_request(
        schema=json_placeholder_schema(schema_type=schema))
    assert response.status == status_code
    assert response.response.get('albumId') == albumId
    assert response.response.get('id') == id
    assert response.response.get('title') == title
    assert response.response.get('url') == url
    assert response.response.get('thumbnailUrl') == thumbnailUrl


def test_users_request():
    response = Request(url=base_url, path='/users/1').json_placeholder_request(
        schema=json_placeholder_schema(schema_type='users'))
    assert response.status == 200
    assert response.response.get('id') == 1
    assert response.response.get('username') == "Bret"


