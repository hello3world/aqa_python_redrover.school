from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    BUTTON_ENTER = (By.XPATH, "//a[text()='Войти']")
    # INPUT_
    # SELECT_
    # CHECKBOX_
    # TEXTAREA_

    # Getter
    def get_button_enter(self):
        # return self.driver.find_element(self.BUTTON_ENTER)
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.BUTTON_ENTER))

    # Actions
    def click_button_enter(self):
        self.get_button_enter().click()

