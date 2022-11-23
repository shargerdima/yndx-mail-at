import time

from pages.main_page import MainPage
from pages.open_page import open_session


class TestLogin:

    def test_login(self, browser, lg='m0r.ya', pw='sharger42571'):
        try:
            open_session(browser)
            mp = MainPage(browser)
            mp.click_input_mail()
            mp.click_mail()
            mp.input_login(lg)
            mp.click_login()
            mp.input_password(pw)
            mp.click_login()
            mp.click_menu()
            mp.should_be_login()

        finally:
            browser.quit()
