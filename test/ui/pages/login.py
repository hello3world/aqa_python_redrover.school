from .base_pages import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)


    def click_on_link_create_account(self):
        ''' Метод кликает по ссылке '''
        self.browser.find_element(*LoginPageLocators.LINK_CREATE_ACCOUNT).click()

