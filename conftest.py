import pytest
from oxwall_application import OxwallApp
from models.user import User



@pytest.fixture()
def app():
    app = OxwallApp(base_url="https://demo.oxwall.com/")
    yield app
    app.close()


@pytest.fixture()
def logged_user(app):
    user = User(username="demo", password="demo")
    app.login(user)
    yield user
    app.logout(user)
