import json
from app import app


def test_openapi_spec():
    client = app.test_client()
    rv = client.get('/openapi.json')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data is not None
    assert 'openapi' in data and data['openapi'].startswith('3.')
    # ensure /yt endpoint is described
    assert '/yt' in data.get('paths', {})
