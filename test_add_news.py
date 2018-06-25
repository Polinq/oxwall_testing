import pytest
from oxwall_application import OxwallApp


@pytest.fixture()
def app():
    app = OxwallApp(base_url="https://demo.oxwall.com/")
    yield app
    app.close()

@pytest.fixture()
def logged_user(app):
    user = "demo"
    password = "demo"
    app.login(user, password)
    yield user
    app.logout(user)

def test_add_text_news(app, logged_user):
    text_news = "New news!"
    old_list_of_news = app.get_list_of_news()
    app.add_new_news(text_news)
    app.wait_new_news_appearing(old_list_of_news)
    assert text_news == app.last_news_text_element().text
    assert logged_user.title() == app.last_news_user_element().text
