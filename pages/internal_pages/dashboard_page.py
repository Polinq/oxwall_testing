from selenium.webdriver.common.by import By

from custom_expected_condition.expected_condition import amount_of_elements_located
from pages.elements.input_field import InputTextElement
from pages.elements.newsfeed import NewsfeedElement
from pages.internal_page import InternalPage


class DashboardPage(InternalPage):
    _NEWSFEEDS = (By.XPATH, "//li[contains(@id,'action-feed')]")
    _NEWS_TEXT_FIELD = (By.NAME, "status")
    _SEND_BUTTON = (By.NAME, "save")

    @property
    def news_text_field(self):
        return InputTextElement(self.find_visible_element(self._NEWS_TEXT_FIELD))

    @property
    def send_button(self):
        return self.find_clickable_element(self._SEND_BUTTON)

    @property
    def newsfeeds(self):
        """ Return list of elements """
        els = [NewsfeedElement(el) for el in self.driver.find_elements(*self._NEWSFEEDS)]
        return els

    def is_here(self):
        #TODO
        return True

    def wait_new_news_appearing(self):
        #  Wait for new news to appear
        self._wait.until(amount_of_elements_located(self._NEWSFEEDS,
                                                   len(self.newsfeeds) + 1))

    def delete_newsfeed(self, newsfeed):
        # newsfeed = self.newsfeeds[number]
        self.move_to_element(newsfeed.webelement)
        self.action.move_to_element(self.driver.find_element_by_css_selector("div.ow_newsfeed_context_menu_wrap")).perform()
        self.action.move_to_element(self.driver.find_element_by_css_selector("div.ow_context_action")).perform()
        self.action.move_to_element(self.driver.find_element_by_css_selector("span.ow_context_more")).perform()
        self.action.move_to_element(self.driver.find_element_by_css_selector("div.ow_context_action")).perform()
        self.move_to_element(newsfeed.context)
        newsfeed.delete_button.click()
        self.alert.accept()
