import unittest, time
from oxwall_application import OxwallApp


class AddNewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = OxwallApp()

    def test_add_text_news(self):
        user = "admin"
        password = "pass"
        text_news = "New news!"
        app = self.app

        app.login(user, password)
        old_list_of_news = app.get_list_of_news()
        app.add_new_news(text_news)
        app.wait_new_news_appearing(old_list_of_news)
        self.assertEqual(text_news, app.last_news_text_element().text)
        self.assertEqual(user.title(), app.last_news_user_element().text)
        app.logout()

    def tearDown(self):
        self.app.close()


if __name__ == "__main__":
    unittest.main()
