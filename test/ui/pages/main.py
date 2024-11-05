from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_pages import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)


    def press_button_become_repetitor(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_BECOME_REPETITOR))
        button.click()