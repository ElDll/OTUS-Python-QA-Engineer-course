from .base_api.api import Request
from .schemas.open_brewery_schema import open_brewery_schema
import pytest


base_url = "https://api.openbrewerydb.org"


def test_single_brewery():
    response = Request(url=base_url, path='/breweries/madtree-brewing-cincinnati').open_brewery_request(
        schema=open_brewery_schema(schema_type="object"))
    assert response.status == 200
    assert response.response.get('id') == 'madtree-brewing-cincinnati'
    assert response.response.get('created_at') == "2021-10-23T02:24:55.243Z"


def test_random_brewery():
    response = Request(url=base_url, path='/breweries/random').open_brewery_request(schema=open_brewery_schema(
        schema_type='array'))
    assert response.status == 200
    assert response.response[0].get('id')
    assert response.response[0].get('name')


@pytest.mark.parametrize('city, schema, id, name',
                         [('san_diego', 'array', 'circle-9-brewing-san-diego', 'Circle 9 Brewing'),
                          ('san_francisco', 'array', 'seven-stills-san-francisco', 'Seven Stills'),
                          ('ulyanovsk', 'empty', None, None)]
                         )
def test_by_city(city, schema, id, name):
    response = Request(url=base_url, path=f'/breweries?by_city={city}&per_page=1').open_brewery_request(
        schema=open_brewery_schema(schema_type=schema))
    assert response.status == 200
    if schema != 'empty':
        assert response.response[0].get('id') == id
        assert response.response[0].get('name') == name


@pytest.mark.parametrize('schema, id, name',
                         [('array', 'circle-9-brewing-san-diego', 'Circle 9 Brewing'),
                          ('array', 'seven-stills-san-francisco', 'Seven Stills'),
                          ('empty', None, 'Hmelnoy house')]
                         )
def test_by_name(schema, id, name):
    response = Request(url=base_url, path=f'/breweries?by_name={name}&per_page=1').open_brewery_request(
        schema=open_brewery_schema(schema_type=schema))
    assert response.status == 200
    if schema != 'empty':
        assert response.response[0].get('id') == id
        assert response.response[0].get('name') == name


@pytest.mark.parametrize('state, schema, id, name',
                         [('new_york', 'array', '12-gates-brewing-company-williamsville', '12 Gates Brewing Company'),
                          ('washington', 'array', 'jc-brewhouse-issaquah', 'JC Brewhouse'),
                          ('ulyanovskya_oblast', 'empty', None, None)]
                         )
def test_by_state(state, schema, id, name):
    response = Request(url=base_url, path=f'/breweries?by_state={state}&per_page=1').open_brewery_request(
        schema=open_brewery_schema(schema_type=schema))
    assert response.status == 200
    if schema != 'empty':
        assert response.response[0].get('id') == id
        assert response.response[0].get('name') == name


