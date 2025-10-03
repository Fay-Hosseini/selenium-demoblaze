import os

import pytest
from pages.login_page import LoginPage

USERNAME = os.environ.get("DEMOBLAZE_USERNAME")
PASSWORD = os.environ.get("DEMOBLAZE_PASSWORD")

def test_login(driver):
    assert USERNAME and PASSWORD, "Please set DEMOBLAZE_USERNAME and DEMOBLAZE_PASSWORD"
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    assert "Welcome" in login.get_logged_user()

