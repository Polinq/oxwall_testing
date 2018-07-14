def test_delete_last_news(app, logged_admin, db):
    old_list_of_news = app.dash_page.newsfeeds
    old_amount_of_news = db.count_news()
    app.dash_page.delete_newsfeed(old_list_of_news[0])
    assert old_amount_of_news - 1 == db.count_news()
    new_list_of_news = app.dash_page.newsfeeds
    new_list_of_news.pop(0)
    assert old_amount_of_news == new_list_of_news
