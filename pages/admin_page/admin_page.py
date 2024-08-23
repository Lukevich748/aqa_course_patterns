import allure
from base.base_page import BasePage
from data.links import Links
from pages.admin_page.components.nationalities import Nationalities
from pages.admin_page.components.user_management.user_management_dropdown import UserManagementDropdown


class AdminPage(BasePage):

    _PAGE_URL = Links.ADMIN_PAGE

    @property
    def menu(self):
        return TopBarMenu(self.driver)


class TopBarMenu(BasePage):

    _USER_MANAGEMENT_DROPDOWN = "//nav[@aria-label='Topbar Menu']//span[text()='User Management ']"
    _NATIONALITIES_TAB = "//nav[@aria-label='Topbar Menu']//a[text()='Nationalities']"

    @allure.step("Open 'User Management' Dropdown")
    def open_user_management_dropdown(self):
        self.click(self._USER_MANAGEMENT_DROPDOWN)

    @property
    def user_management_dropdown(self):
        return UserManagementDropdown(self.driver)

    @property
    def nationalities(self):
        return Nationalities(self.driver)

    @allure.step("Open 'Nationalities' Tab")
    def open_nationalities(self):
        self.click(self._NATIONALITIES_TAB)