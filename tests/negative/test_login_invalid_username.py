import os
from pages.login_page import LoginPage

INVALID_USERNAME = os.environ.get("DEMOBLAZE_INVALID_USERNAME")
PASSWORD = os.environ.get("DEMOBLAZE_PASSWORD")

def test_login_failed(driver):
    assert INVALID_USERNAME and PASSWORD, "Please set DEMOBLAZE_USERNAME and DEMOBLAZE_PASSWORD"
    login = LoginPage(driver)
    login.login(INVALID_USERNAME, PASSWORD)

    assert "User does not exist." in login.get_failed_user()
