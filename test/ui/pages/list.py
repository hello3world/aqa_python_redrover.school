from .base_pages import BasePage
from .locators import LoginPageLocators


class ListPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_match_current_url (self):
        assert self.browser.current_url == "http://195.133.27.184/list/", f"страница {self.browser.current_url} не соответсвует заданной"

