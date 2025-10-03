from pages.home_page import  HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_checkout(driver):
    home = HomePage(driver)
    home.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open_cart()
    cart.checkout("John Doe", "USA", "NYC", "1234567890123456", "12", "2025")

    confirmation = cart.get_confirmation()
    assert "Thank you" in confirmation

