from flask import Flask

from handlers.routes import configure_routes

app = Flask(__name__)
configure_routes(app)
client = app.test_client()
url = "/"


def test_base_route_once():
    response = client.get(url)

    assert response.get_data() == b'{"counter":1,"value":0}\n'
    assert response.status_code == 200


def test_base_route_twice():
    response = client.get(url)

    assert response.get_data() == b'{"counter":2,"value":1}\n'
    assert response.status_code == 200


def test_base_route_three_times():
    response = client.get(url)

    assert response.get_data() == b'{"counter":3,"value":1}\n'
    assert response.status_code == 200

def test_base_route_four_times():
    response = client.get(url)

    assert response.get_data() == b'{"counter":4,"value":2}\n'
    assert response.status_code == 200
