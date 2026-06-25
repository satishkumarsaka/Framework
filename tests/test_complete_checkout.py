from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage

def test_checkout_flow(driver):
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.click_cart()

    assert "cart" in driver.current_url

    cart = CartPage(driver)
    cart.click_checkout()

    assert "checkout-step-one" in driver.current_url

    info = InfoPage(driver)
    info.enter_first_name("Satish")
    info.enter_last_name("Kumar")
    info.enter_zip_code("12345")
    info.click_continue()

    assert "checkout-step-two" in driver.current_url

    overview = OverviewPage(driver)
    overview.click_finish()

    assert "checkout-complete" in driver.current_url

    complete = CompletePage(driver)
    assert complete.get_message_text() == "Thank you for your order!"