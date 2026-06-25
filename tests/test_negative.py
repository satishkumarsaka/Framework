from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username, password, expected", [
    ("wrong_user", "wrong_pass", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out")
])

def test_invalid_login(driver, username, password, expected):
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    assert expected in login.get_error_text()