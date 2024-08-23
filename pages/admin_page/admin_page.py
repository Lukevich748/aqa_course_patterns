import allure
from base.base_page import BasePage
from data.links import Links
from helpers.ui_helper import UIHelper
from pages.admin_page.components.nationalities import Nationalities
from pages.admin_page.components.user_management_dropdown import UserManagementDropdown


class AdminPage(BasePage):

    _PAGE_URL = Links.ADMIN_PAGE

    _NATIONALITIES_TAB = "//nav[@aria-label='Topbar Menu']//a[text()='Nationalities']"
    _USER_MANAGEMENT_DROPDOWN = "//nav[@aria-label='Topbar Menu']//span[text()='Job ']"

    def __init__(self, driver):
        super().__init__(driver)

        self.nationalities = Nationalities(self.driver)


    @allure.step("Open 'Job' Tab")
    def user_management_dropdown(self):
        self.click(self._USER_MANAGEMENT_DROPDOWN)


    @allure.step("Open 'Nationalities' Tab")
    def open_nationalities(self):
        self.click(self._NATIONALITIES_TAB)


