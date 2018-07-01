from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.main_page import MainPage
from pages.login_window import LoginWindow


class OxwallApp:
    def __init__(self, base_url="http://127.0.0.1/oxwall/"):
        # Open Oxwall UI in browser
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = base_url
        self.driver.get(self.base_url)

        self.main_page = MainPage(self.driver)
        self.login_window = LoginWindow(self.driver)
        self.dash_page = DashboardPage(self.driver)

    def close(self):
        self.driver.quit()

    def login(self, user):
        self.main_page.sign_in_link.click()
        username_field = self.login_window.username_field
        username_field.clear()
        username_field.send_keys(user.username)
        password_field = self.login_window.password_field
        password_field.clear()
        password_field.send_keys(user.password)
        self.login_window.click_sing_in_btn()

    def go_to_members_page(self):
        # TODO change to Page Object
        self.driver.find_element_by_link_text("MEMBERS").click()

    def logout(self, user):
        # TODO change to Page Object
        driver = self.driver
        ActionChains(driver).move_to_element(driver.find_element_by_link_text(user.username.title())).perform()
        driver.find_element_by_link_text("Sign Out").click()

    def add_new_news(self, news):
        news_text_field = self.dash_page.news_text_field
        news_text_field.clear()
        news_text_field.send_keys(news.text)
        self.dash_page.send_button.click()

    def last_news_user_element(self):
        # TODO It will be removed. Not needed in Page Element Object concept
        return self.driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[2]/a/b")

    def last_news_text_element(self):
        # TODO It will be removed. Not needed in Page Element Object concept
        return self.driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]")

    def wait_new_news_appearing(self, old_list_of_news):
        #  Wait for new news to appear
        self.dash_page.wait_new_news_appearing()
