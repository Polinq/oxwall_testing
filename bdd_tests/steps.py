from pytest_bdd import given, when, then
from models.news import News


@given("initial news in Oxwall database")
def old_news_in_db(db):
    return db.count_news()


@given("I as a logged admin")
def logged_admin(app, admin):
    app.login(admin)
    yield admin
    app.logout()


@given("a news with text <text> and without any photo")
def news(text):
    return News(text=text)


@when("I add the news")
def add_news(app, news):
    app.add_new_news(news)


@then("a new newsfeed block appears before old list of news")
def wait_new_news(app):
    assert app.dash_page.wait_new_news_appearing()


@then("this newsfeed block is with this text and author as Admin")
def verify_newsfeed_block(app, db, news, old_news_in_db, logged_admin):
    assert old_news_in_db + 1 == db.count_news()
    assert news.text == db.get_last_news().text, "Not correct text"
    assert news.text == app.dash_page.newsfeeds[0].news_text
    assert logged_admin.username.title() == app.dash_page.newsfeeds[0].user
