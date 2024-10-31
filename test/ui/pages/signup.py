from .base_pages import BasePage
from .locators import LoginPageLocators, SignUpPageLocators


class SignUpPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def enter_username(self, username):
        self.browser.find_element(*SignUpPageLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(*SignUpPageLocators.PASSWORD).send_keys(password)

    def enter_password_confirm(self, password):
        self.browser.find_element(*SignUpPageLocators.PASSWORD_CONFIRM).send_keys(password)

    def press_on_link_create_account(self):
        self.browser.find_element(
            *SignUpPageLocators.LINK_TO_REGISTER).click()


