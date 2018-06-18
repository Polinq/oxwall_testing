from selenium import webdriver


class OxwallApp:
    def __init__(self):
        # Open Oxwall UI in browser
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.base_url = "http://127.0.0.1/oxwall/"
        self.driver.get(self.base_url)

    def login(self, user):
        pass

    def go_to_members_page(self):
        self.driver.find_element_by_link_text("MEMBERS").click()

    def add_new_news(self, text):
        pass

    def logout(self):
        pass


if __name__ == "__main__":
    app = OxwallApp()
    app.go_to_members_page()
    app.driver.quit()
