from models.news import News
import pytest

news_list = [
    News(text="New news!"),
    News(text="Привет!")
]


@pytest.mark.parametrize("news", news_list, ids=[repr(news) for news in news_list])
def test_add_text_news(app, logged_user, news):
    old_list_of_news = app.get_list_of_news()
    app.add_new_news(news)
    app.wait_new_news_appearing(old_list_of_news)
    assert news.text == app.last_news_text_element().text
    assert logged_user.username.title() == app.last_news_user_element().text


def test_add_news_with_photo(app, logged_user):
    pass
