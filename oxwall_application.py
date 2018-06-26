from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from custom_expected_condition.expected_condition import amount_of_elements_located


class OxwallApp:
    def __init__(self, base_url="http://127.0.0.1/oxwall/"):
        # Open Oxwall UI in browser
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = base_url
        self.driver.get(self.base_url)

    def close(self):
        self.driver.quit()

    def login(self, user):
        driver = self.driver
        # initiate login
        driver.find_element_by_css_selector("span.ow_signin_label").click()
        username_field = driver.find_element_by_name("identity")
        username_field.clear()
        username_field.send_keys(user.username)
        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(user.password)
        driver.find_element_by_name("submit").click()
        # Wait until login finished
        self.wait.until_not(visibility_of_element_located((By.ID, "floatbox_overlay")))


    def go_to_members_page(self):
        self.driver.find_element_by_link_text("MEMBERS").click()

    def logout(self, user):
        driver = self.driver
        ActionChains(driver).move_to_element(driver.find_element_by_link_text(user.username.title())).perform()
        driver.find_element_by_link_text("Sign Out").click()

    def add_new_news(self, news):
        driver = self.driver
        news_text_field = driver.find_element_by_name("status")
        # news_text_field.click()
        news_text_field.clear()
        news_text_field.send_keys(news.text)
        driver.find_element_by_name("save").click()

    def last_news_user_element(self):
        return self.driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[2]/a/b")

    def last_news_text_element(self):
        return self.driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]")

    def wait_new_news_appearing(self, old_list_of_news):
        #  Wait for new news to appear
        self.wait.until(amount_of_elements_located((By.XPATH, "//li[contains(@id,'action-feed')]"),
                                                   len(old_list_of_news) + 1))

    def get_list_of_news(self):
        return self.driver.find_elements_by_xpath("//li[contains(@id,'action-feed')]")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    accept_next_alert = True
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

if __name__ == "__main__":
    app = OxwallApp()
    app.login("admin", "pass")
    app.add_new_news("World is wonderful!")
    app.go_to_members_page()
    app.driver.quit()
