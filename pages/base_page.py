from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://mail.yandex.ru"

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

