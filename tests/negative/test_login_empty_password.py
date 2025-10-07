import os
from pages.login_page import LoginPage

USERNAME= os.environ.get("DEMOBLAZE_USERNAME")
NO_PASSWORD = ""

def test_login_failed(driver):

    login = LoginPage(driver)
    login.login(USERNAME, NO_PASSWORD)

    assert "Please fill out Username and Password." in login.get_failed_user()
