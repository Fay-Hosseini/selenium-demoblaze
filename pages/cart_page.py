from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_LINK = (By.ID, "cartur")
    # DELETE_BTN = (By.LINK_TEXT, "Delete")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Place Order']")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CREDIT_CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BTN = (By.XPATH, "//button[text()='Purchase']")
    CONFIRMING_MSG = (By.XPATH, "//h2[text()='Thank you for your purchase!']")


    def open_cart(self):
        self.click(self.CART_LINK)

    def checkout(self,name, country, city, card,month, year):
        self.click(self.PLACE_ORDER_BTN)
        self.type(self.NAME_INPUT, name)
        self.type(self.COUNTRY_INPUT, country)
        self.type(self.CITY_INPUT, city)
        self.type(self.CREDIT_CARD_INPUT, card)
        self.type(self.MONTH_INPUT, month)
        self.type(self.YEAR_INPUT, year)
        self.click(self.PURCHASE_BTN)

    def get_confirmation(self):
        return self.get_text(self.CONFIRMING_MSG)
