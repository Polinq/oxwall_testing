import pytest
from oxwall_application import OxwallApp


@pytest.fixture()
def app():
    app = OxwallApp(base_url="https://demo.oxwall.com/")
    yield app
    app.close()


def test_add_text_news(app):
    user = "demo"
    password = "demo"
    text_news = "New news!"

    app.login(user, password)
    old_list_of_news = app.get_list_of_news()
    app.add_new_news(text_news)
    app.wait_new_news_appearing(old_list_of_news)
    assert text_news == app.last_news_text_element().text
    assert user.title() == app.last_news_user_element().text
    app.logout(user)

