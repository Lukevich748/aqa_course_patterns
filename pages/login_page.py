import allure
from data.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _USER_NAME_FILED = "//input[@name='username']"
    _PASSWORD_FILED = "//input[@name='password']"
    _LOGIN_BUTTON = "//button[@type='submit']"

    @allure.step("Enter user name")
    def enter_user_name(self, user_name):
        user_name_field = self.wait.until(EC.element_to_be_clickable(self._USER_NAME_FILED))
        user_name_field.clear()
        user_name_field.send_keys(user_name)
        assert user_name == user_name_field.get_attribute("value"), f"The username field does not contain '{user_name}'"

    @allure.step("Enter password")
    def enter_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self._PASSWORD_FILED))
        password_field.clear()
        password_field.send_keys(password)
        assert password == password_field.get_attribute("value"), f"The password field does not contain '{password}'"

    @allure.step("Click 'Login' button")
    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        login_button.click()
        assert self.wait.until(EC.url_to_be(Links.DASHBOARD_PAGE))