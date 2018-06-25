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
    user = User(username="demo", password = "demo")
    app.login(user)
    yield user
    app.logout(user)


def test_add_text_news(app, logged_user):
    text_news = "New news!"
    old_list_of_news = app.get_list_of_news()
    app.add_new_news(text_news)
    app.wait_new_news_appearing(old_list_of_news)
    assert text_news == app.last_news_text_element().text
    assert logged_user.username.title() == app.last_news_user_element().text


def test_add_news_with_photo(app, logged_user):
    pass
