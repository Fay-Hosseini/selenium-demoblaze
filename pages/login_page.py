from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[onclick='logIn()']")
    CLOSE_BTN = (By.XPATH, "//button[text()='Close']")
    LOGGED_USER = (By.ID, "nameofuser")


    def login(self,username, password):
        self.click(self.LOGIN_LINK)
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)


    def get_logged_user(self):
        element = self.wait.until(EC.visibility_of_element_located(self.LOGGED_USER))
        # wait until text contains "Welcome"
        self.wait.until(lambda d: element.text.startswith("Welcome"))
        return element.text

    def get_failed_user(self):
        """
        Waits for the error message and returns its text.
        Used when login fails due to invalid username or password.
        """
        # Wait for JavaScript alert to appear
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # close the alert
        return alert_text





