import os
import pickle
import allure
from data.credentials import Credentials
from data.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _USER_NAME_FILED = "//input[@name='username']"
    _PASSWORD_FILED = "//input[@name='password']"
    _LOGIN_BUTTON = "//button[@type='submit']"

    def successful_login(self):
        if os.path.exists("cookies.pkl"):
            self.driver.delete_all_cookies()

            with open("cookies.pkl", "rb") as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
        else:
            self.enter_user_name(Credentials.LOGIN)
            self.enter_password(Credentials.PASSWORD)
            self.enter_password()

            with open("cookies.pkl", "wb") as cookies_file:
                pickle.dump(self.driver.get_cookies(), cookies_file)

    @allure.step("Enter user name")
    def enter_user_name(self, user_name):
        self.wait_element_to_be_clickable(self._USER_NAME_FILED)
        self.find(self._USER_NAME_FILED).clear()
        self.fill(self._USER_NAME_FILED, user_name)
        assert user_name == self.find(self._USER_NAME_FILED).get_attribute("value"), f"The user name field does not contain '{user_name}'"

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait_element_to_be_clickable(self._PASSWORD_FILED)
        self.find(self._PASSWORD_FILED).clear()
        self.fill(self._PASSWORD_FILED, password)
        assert password == self.find(self._PASSWORD_FILED).get_attribute("value"), f"The password field does not contain '{password}'"

    @allure.step("Click on 'Login' button")
    def click_login_button(self):
        self.wait_element_to_be_clickable(self._LOGIN_BUTTON)
        self.click(self._LOGIN_BUTTON)
        assert self.wait.until(EC.url_to_be(Links.DASHBOARD_PAGE)), "The URL did not change to the expected"