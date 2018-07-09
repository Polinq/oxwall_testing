import pytest
from oxwall_application import OxwallApp
from models.user import User
import json
import os.path

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json", help="config file")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    filename = os.path.join(PROJECT_DIR, filename)
    with open(filename) as f:
        return json.load(f)


@pytest.fixture()
def app(selenium, config):
    app = OxwallApp(driver=selenium, base_url=config["base_url"])
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
