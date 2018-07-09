from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable


class Page:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException as e:
            return False
        return True

    def find_visible_element(self, locator):
        return self._wait.until(visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self._wait.until(element_to_be_clickable(locator))

    def move_to_element(self, element):
        self.action.move_to_element(element).perform()

    @property
    def current_url(self):
        # TODO need correction. It depends on base_url
        return self.driver.current_url

