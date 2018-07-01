from models.news import News
import pytest
from data.news_data import news_list


@pytest.fixture(params=news_list, ids=[repr(news) for news in news_list])
def news(request):
    return News(**request.param)


def test_add_text_news(app, logged_user, news):
    old_list_of_news = app.get_list_of_news()
    app.add_new_news(news)
    app.wait_new_news_appearing(old_list_of_news)
    assert news.text == app.last_news_text_element().text
    assert logged_user.username.title() == app.last_news_user_element().text


def test_add_news_with_photo(app, logged_user):
    pass
