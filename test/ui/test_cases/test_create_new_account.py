import time

import pytest

from test.ui.pages.list import ListPage
from test.ui.pages.login import LoginPage
from test.ui.pages.main import MainPage
from test.ui.pages.signup import SignUpPage

class TestCreateNewAccount:

    @pytest.mark.smoke
    def test_guest_can_create_new_account(self, browser, user_data):
        url = 'http://195.133.27.184/'

        main_page = MainPage(browser, url)
        main_page.open()
        main_page.press_button_become_repetitor()

        login = LoginPage(browser, url)
        login.click_on_link_create_account()

        sign_up_page = SignUpPage(browser, url)
        sign_up_page.enter_username(user_data["username"])
        sign_up_page.enter_password(user_data["password"])
        sign_up_page.enter_password_confirm(user_data["password"])
        sign_up_page.press_on_link_create_account()
        time.sleep(5)
        list_page = ListPage(browser, url)
        list_page.should_match_current_url()