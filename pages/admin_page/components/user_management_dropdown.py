import allure
from base.base_page import BasePage


class UserManagementDropdown(BasePage):

    _USERS_TAB = "//a[text()='Users']"

    @allure.step("Open 'Users' Tab")
    def open_users(self):
        self.click(self._USERS_TAB)