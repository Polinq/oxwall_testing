from models.news import News
import pytest
from data.news_data import news_list


@pytest.fixture(params=news_list, ids=[repr(news) for news in news_list])
def news(request):
    return News(**request.param)


def test_add_text_news(app, logged_admin, news, db):
    # old_list_of_news = app.dash_page.newsfeeds
    old_amount_of_news = db.count_news()
    app.add_new_news(news)
    app.dash_page.wait_new_news_appearing()
    assert old_amount_of_news + 1 == db.count_news()
    assert news.text == db.get_last_news().text
    assert news.text == app.dash_page.newsfeeds[0].news_text
    assert logged_admin.username.title() == app.dash_page.newsfeeds[0].user


def test_add_news_with_photo(app, logged_admin):
    pass
