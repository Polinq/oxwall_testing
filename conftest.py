import pytest
from oxwall_application import OxwallApp
from models.user import User
import json


@pytest.fixture(scope="session")
def config():
    with open("config.json") as f:
        return json.load(f)


@pytest.fixture()
def app(config):
    app = OxwallApp(base_url=config["base_url"])
    yield app
    app.close()


@pytest.fixture()
def logged_user(app, config):
    user = User(**config["admin"])
    app.login(user)
    yield user
    app.logout(user)
