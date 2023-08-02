import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    services = Service(executable_path='C:/Users/Анастасия/WebDriver/bin/geckodriver-v0.33.0-win32/geckodriver.exe')
    browser = webdriver.Firefox(service=services)
    browser.maximize_window()
    yield browser
    browser.quit()
