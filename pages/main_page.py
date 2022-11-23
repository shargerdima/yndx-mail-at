from pages.base_page import BasePage
from pages.locators import PageLocators


class MainPage(BasePage):
    def click_input_mail(self):
        assert self.element_present(*PageLocators.BT_NoLogin), 'Кнопка Войти в Почту не найдена'
        self.browser.find_element(*PageLocators.BT_NoLogin).click()

    def click_mail(self):
        assert self.element_present(*PageLocators.BT_Mail), 'Кнопка Почта не найдена'
        self.browser.find_element(*PageLocators.BT_Mail).click()

    def input_login(self, text):
        assert self.element_present(*PageLocators.FD_Login), 'Поле Логин или email не найдена'
        inpt = self.browser.find_element(*PageLocators.FD_Login)
        inpt.click()
        inpt.send_keys(text)

    def input_password(self, text):
        assert self.element_present(*PageLocators.FD_Password)
        inpt = self.browser.find_element(*PageLocators.FD_Password)
        inpt.click()
        inpt.send_keys(text)

    def click_login(self):
        assert self.element_present(*PageLocators.BT_Login)
        bt = self.browser.find_element(*PageLocators.BT_Login)
        bt.click()

    def click_menu(self):
        assert self.element_present(*PageLocators.BT_User_Menu)
        bt = self.browser.find_element(*PageLocators.BT_User_Menu)
        bt.click()

    def get_login_in_menu(self, text):
        assert self.browser.find_element_by_xpath(f"//*[@class='legouser__menu-header']//*[@class='user-account__name'"
                                                f" and text()='{text}']")
        el = self.browser.find_element_by_xpath(f"//*[@class='legouser__menu-header']//*[@class='user-account__name'"
                                                f" and text()='{text}']")
        return el

    def should_be_login(self):
        assert self.element_present(*PageLocators.TX_USER_NAME)
        login = self.browser.find_element(*PageLocators.TX_USER_NAME)
        print(login.text)
        if login.text == 'm0r.ya':
            print("Авторизация прошла успешно")
        else:
            print("Авторизация не прошла")
        # assert login.text == 'm0r.ya'
        # login = self.get_login_in_menu(text)
        # print('Логин: ' + login.text)
        # if login.text == text:
        #     print("Авторизация прошла успешно")
        # else:
        #     print("Авторизация не прошла")
        # assert login.text == text
