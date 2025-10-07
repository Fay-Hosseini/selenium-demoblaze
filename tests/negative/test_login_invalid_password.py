import os
from pages.login_page import LoginPage
from tests.negative.test_login_invalid_username import INVALID_USERNAME

USERNAME = os.environ.get("DEMOBLAZE_USERNAME")
INVALID_PASSWORD = os.environ.get("DEMOBLAZE_INVALID_PASSWORD")

def test_login_failed(driver):
    assert USERNAME and INVALID_PASSWORD, "Please set DEMOBLAZE_USERNAME and DEMOBLAZE_PASSWORD"
    login = LoginPage(driver)
    login.login(USERNAME, INVALID_PASSWORD)

    assert "Wrong password." in login.get_failed_user()
