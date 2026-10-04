from app import app


def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Hello, World' in response.data


def test_version():
    response = app.test_client().get('/version')
    assert response.status_code == 200
    assert b'1.0' in response.data


def test_test_endpoint():
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert b'/test' in response.data
