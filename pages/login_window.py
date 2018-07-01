from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from pages.base_page import Page


class LoginWindow(Page):
    _USERNAME_FIELD = (By.NAME, "identity")
    _PASSWORD_FIELD = (By.NAME, "password")
    _SING_IN_BUTTON = (By.NAME, "submit")
    _DARK_OVERLAY = (By.ID, "floatbox_overlay")
    _LOGIN_WINDOW = ()

    @property
    def username_field(self):
        return self.find_visible_element(self._USERNAME_FIELD)

    @property
    def password_field(self):
        return self.find_visible_element(self._PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return self.find_visible_element(self._SING_IN_BUTTON)

    def is_here(self):
        return self.is_element_present(self._DARK_OVERLAY)

    def click_sing_in_btn(self):
        self.sign_in_button.click()
        self._wait.until_not(visibility_of_element_located(self._DARK_OVERLAY))

    def login_as(self, user):
        self.username_field.send_keys(user.username)
        self.password_field.send_keys(user.password)
        self.sign_in_button()
