import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_client():
    url = "<https://example.com/api/login>"
    data = {"username": "testuser", "password": "testpass"}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    token = response.json().get("token")

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session