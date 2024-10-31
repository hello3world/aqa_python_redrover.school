import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from faker import Faker

fake = Faker()

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def user_data():
    username = fake.user_name()
    password = fake.password()
    return {"username": username, "password": password}
