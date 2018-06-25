from models.news import News


def test_add_text_news(app, logged_user):
    news = News(text="New news!")
    old_list_of_news = app.get_list_of_news()
    app.add_new_news(news)
    app.wait_new_news_appearing(old_list_of_news)
    assert news.text == app.last_news_text_element().text
    assert logged_user.username.title() == app.last_news_user_element().text


def test_add_news_with_photo(app, logged_user):
    pass
