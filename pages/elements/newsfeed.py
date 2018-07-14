from selenium.webdriver.common.by import By


class NewsfeedElement:
    _USER = (By.CSS_SELECTOR, ".ow_newsfeed_string.ow_small.ow_smallmargin")
    _CONTENT = (By.CSS_SELECTOR, ".ow_newsfeed_content.ow_smallmargin")
    _TIME = (By.CSS_SELECTOR, ".ow_nowrap.create_time.ow_newsfeed_date.ow_small")
    # _CONTEXT = (By.CSS_SELECTOR, "span.ow_context_more")
    _CONTEXT = (By.CSS_SELECTOR, "div.ow_context_action")
    _DELETE_BUTTON = (By.LINK_TEXT, "Delete post")

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

    @property
    def context(self):
        return self.webelement.find_element(*self._CONTEXT)

    @property
    def delete_button(self):
        return self.webelement.find_element(*self._DELETE_BUTTON)

    def __eq__(self, other):
        return (
                self.news_text == other.news_text
                and self.user == self.user
                and self.time == self.time
                )
