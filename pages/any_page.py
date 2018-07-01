from selenium.webdriver.common.by import By
from pages.base_page import Page


class AnyPage(Page):
    _OXWALL_LOGO = (By.CSS_SELECTOR, "div.ow_footer a > img")

    @property
    def logo(self):
        return self.driver.find_element(*self._OXWALL_LOGO)


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall/")
    page = AnyPage(driver)
    page.logo.click()
