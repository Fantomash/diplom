class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def add_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()