from pages.base_page import BasePage


def open_session(browser):
    print('Открываем браузер')
    page = BasePage(browser)
    page.open()
