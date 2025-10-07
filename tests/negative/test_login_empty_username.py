import os
from pages.login_page import LoginPage

NO_USERNAME=""
PASSWORD = os.environ.get("DEMOBLAZE_PASSWORD")

def test_login_failed(driver):

    login = LoginPage(driver)
    login.login(NO_USERNAME, PASSWORD)

    assert "Please fill out Username and Password." in login.get_failed_user()
