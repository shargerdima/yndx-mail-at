from selenium.webdriver.common.by import By


class PageLocators:
    BT_NoLogin = (By.XPATH, "//*[@type='button']")
    BT_Mail = (By.XPATH, "//*[text()='Почта']/parent::button")
    FD_Login = (By.XPATH, "//*[@id='passp-field-login']")
    FD_Password = (By.XPATH, "//*[@id='passp-field-passwd']")
    BT_Login = (By.XPATH, "//*[@id='passp:sign-in']")
    BT_User_Menu = (By.XPATH, "//*[contains(@class, 'legouser_fetch-accounts_yes')]")
    TX_USER_NAME = (By.XPATH, "//*[@class='user-account__name']//preceding-sibling::text()")
