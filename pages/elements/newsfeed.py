from selenium.webdriver.common.by import By


class NewsfeedElement:
    _USER = (By.CSS_SELECTOR, ".ow_newsfeed_string.ow_small.ow_smallmargin")
    _CONTENT = (By.CSS_SELECTOR, ".ow_newsfeed_content.ow_smallmargin")
    _TIME = (By.CSS_SELECTOR, ".ow_nowrap.create_time.ow_newsfeed_date.ow_small")

    def __init__(self, webelement):
        self.webelement = webelement

    @property
    def user(self):
        return self.webelement.find_element(*self._USER).text

    @property
    def news_text(self):
        return self.webelement.find_element(*self._CONTENT).text

    @property
    def time(self):
        return self.webelement.find_element(*self._TIME).text
