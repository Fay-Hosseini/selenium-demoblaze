from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
        # wait up to 10 seconds for alert to appear
        try:
            wait = WebDriverWait(self.driver, 10)
            alert = wait.until(EC.alert_is_present())

            # 3. Accept (dismiss) the alert
            alert_text = alert.text
            alert.accept()
            # Optionally, assert the alert text here for better reporting
            assert "Product added" in alert_text

        except TimeoutException:
            # Handle case where the alert doesn't appear
            print("Alert did not appear after clicking 'Add to cart'.")
            raise