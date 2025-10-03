from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)