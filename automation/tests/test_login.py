import pytest
from pages.login_page import LoginPage


class TestLogin:

    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """TC-01: Valid Credentials should reach products page"""
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html", \
            "Expected to be in products page after login"

    @pytest.mark.smoke
    def test_locked_out_user(self, driver):
        """TC-02: locked_out_user should show error message"""
        page = LoginPage(driver)
        page.login("locked_out_user", "secret_sauce")
        error = page.get_error_message()
        assert "locked out" in error, \
            "Expected to have user locked out text in the error message"

    @pytest.mark.regression
    def test_wrong_password(self, driver):
        """TC-03: Wrong password should show error"""
        page = LoginPage(driver)
        page.login("standard_user", "sauce")
        error = page.get_error_message()
        assert "password" in error, \
            "Expected to show error message regarding invalid password or mismatch"

    @pytest.mark.regression
    def test_empty_username(self, driver):
        """TC-04: Empty username should show error"""
        page = LoginPage(driver)
        page.login("", "secret_sauce")
        error = page.get_error_message()
        assert "Username is required" in error, \
            "Expected to show error message of empty username"

    @pytest.mark.regression
    def test_empty_password(self, driver):
        """TC-05: Empty password should show error"""
        page = LoginPage(driver)
        page.login("standard_user", "")
        error = page.get_error_message()
        assert "Password is required" in error, \
            "Expected to show error message of empty password"

    @pytest.mark.regression
    def test_empty_both_fields(self, driver):
        """TC-06: Both fields empty should show error"""
        page = LoginPage(driver)
        page.login("", "")
        error = page.get_error_message()
        assert "Username is required" in error, \
            "Expected to show error message regarding empty fields"

    @pytest.mark.regression
    def test_error_message_text_wrong_password(self, driver):
        """TC-07: Error message text is correct"""
        page = LoginPage(driver)
        page.login("standard_user", "wrongpassword")
        error = page.get_error_message()
        assert "Epic sadface: Username and password do not match any user in this service" in error, \
            "Expected to the show the complete error message"

    @pytest.mark.regression
    def test_successful_login_url(self, driver):
        """TC-08: URL contains 'inventory' after valid login"""
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url, \
            "Expected to have inventory text in the URL after login"
