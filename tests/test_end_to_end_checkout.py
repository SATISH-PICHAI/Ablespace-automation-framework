from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_complete_checkout_flow():

    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    # Cart
    cart = CartPage(driver)
    cart.click_checkout()

    # Checkout Information
    checkout_info = CheckoutInfoPage(driver)
    checkout_info.enter_information("Satish", "QA", "560001")

    # Checkout Overview
    overview = CheckoutOverviewPage(driver)
    total = overview.get_total_amount()
    print("Order Total:", total)

    assert "Total" in total

    overview.click_finish()

    # Checkout Complete
    complete = CheckoutCompletePage(driver)
    message = complete.get_success_message()

    assert message == "Thank you for your order!"

    driver.quit()
