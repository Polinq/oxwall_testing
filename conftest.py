import pytest
from oxwall_application import OxwallApp
from models.user import User
import json
import os.path

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def config():
    filename = os.path.join(PROJECT_DIR, "config.json")
    with open(filename) as f:
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


@pytest.fixture()
def admin(config):
    return User(**config["admin"])
