import allure
from base.base_page import BasePage
from pages.admin_page.components.user_management.components.users import Users


class UserManagementDropdown(BasePage):

    _USERS_TAB = "//a[text()='Users']"

    @property
    def users(self):
        return Users(self.driver)

    @allure.step("Open 'Users' Tab")
    def open_users(self):
        self.click(self._USERS_TAB)