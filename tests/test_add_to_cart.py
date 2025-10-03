import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.open_first_product()
    product.add_to_cart()
    cart.open_cart()

    # assert "Delete" in driver.page_source  # product added

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Delete"))
        )
        assert "Delete" in driver.page_source
        print("Test passed: Product is confirmed in the cart.")
    except TimeoutException:
        pytest.fail("Test failed: 'Delete' link not found, product was not successfully added to the cart table.")