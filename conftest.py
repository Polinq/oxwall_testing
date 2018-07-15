import pytest
from fixtures.oxwall_application import OxwallApp
from fixtures.oxwall_db_fixture import OxwallDB
from models.user import User
import json
import os.path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json", help="config file")
    parser.addoption("--browser", action="store", default="Chrome")


@pytest.fixture()
def driver(request):
    option = request.config.getoption("--browser")
    if option.lower() == "chrome":
        return webdriver.Chrome(ChromeDriverManager().install())
    elif option == "firefox":
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif option == "edge":
        return webdriver.Edge(EdgeDriverManager().install())
    elif option == "ie":
        return webdriver.Ie(IEDriverManager().install())
    else:
        raise ValueError("Unrecognized browser {}".format(option))


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    filename = os.path.join(PROJECT_DIR, filename)
    with open(filename) as f:
        return json.load(f)


@pytest.fixture()
def app(driver, config, request):
    base_url = request.config.getoption("--base-url")
    app = OxwallApp(driver=driver, base_url=base_url)
    yield app
    app.close()


@pytest.fixture()
def admin(config):
    return User(**config["web"]["admin"])


@pytest.fixture()
def logged_admin(app, admin):
    app.login(admin)
    yield admin
    app.logout()


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(config["db"])
    yield db
    db.connection.close()


@pytest.fixture()
def regular_user(db):
    user = User(username="test123", password="test", email="tester123@gmail.com")
    db.create_user(user)
    yield user
    db.delete_user(user)
