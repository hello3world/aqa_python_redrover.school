from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_BECOME_REPETITOR = (By.LINK_TEXT, "Стать репетитором")

class LoginPageLocators:
    LINK_CREATE_ACCOUNT = (By.LINK_TEXT, "Создать аккаунт")

class SignUpPageLocators:
    USERNAME = (By.ID, "id_username")
    PASSWORD = (By.ID, "id_password1")
    PASSWORD_CONFIRM = (By.ID, "id_password2")
    LINK_TO_REGISTER = (By.XPATH, '//*[text() = "Зарегистрироваться"]')
