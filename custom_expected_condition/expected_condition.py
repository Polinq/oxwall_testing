class amount_of_elements_located(object):
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.number:
            return elements
        else:
            return False
