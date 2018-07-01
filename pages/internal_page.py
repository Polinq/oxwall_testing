from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import Page


class InternalPage(Page):
    # Navigation
    _DASHBOARD_LINK = (By.LINK_TEXT, "DASHBOARD")
    _MAIN_LINK = (By.LINK_TEXT, "MAIN")
    _JOIN_LINK = (By.LINK_TEXT, "JOIN")
    _MEMBERS_LINK = (By.LINK_TEXT, "MEMBERS")
    _PHOTO_LINK = (By.LINK_TEXT, "PHOTO")
    _VIDEO_LINK = (By.LINK_TEXT, "VIDEO")
    # Sign in, Sign up
    _SIGN_IN_LINK = (By.CSS_SELECTOR, "span.ow_signin_label")
    _SIGN_UP_LINK = ()
    # User menu and notification

    def is_logged_in(self):
        return True if self.is_element_present(self._DASHBOARD_LINK) else False

    @property
    def sign_in_link(self):
        if not self.is_logged_in():
            return self.find_clickable_element(self._SIGN_IN_LINK)
        else:
            raise NoSuchElementException("No element with {}. Maybe it is logged in".format(self._SIGN_IN_LINK))