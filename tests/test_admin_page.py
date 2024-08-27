import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest
from faker import Faker

fake = Faker()


@allure.epic("System Administration")
class TestAdminPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.feature("Nationality Management")
    @allure.story("Add Nationality")
    @allure.title("Add a New Nationality")
    def test_add_nationality(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.successful_login()
        self.dashboard_page.is_opened()
        self.dashboard_page.open_admin_tab()
        self.admin_page.is_opened()
        self.admin_page.menu.open_nationalities()
        self.admin_page.menu.nationalities.click_add_nationality_button()
        self.admin_page.menu.nationalities.enter_nationality_name(fake.country())
        self.admin_page.menu.nationalities.click_save_button()

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.feature("User Management")
    @allure.story("Search User")
    @allure.title("Search User by User Name")
    def test_search_user_name(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.successful_login()
        self.dashboard_page.is_opened()
        self.dashboard_page.open_admin_tab()
        self.admin_page.is_opened()
        self.admin_page.menu.open_user_management_dropdown()
        self.admin_page.menu.user_management_dropdown.open_users()
        self.admin_page.menu.user_management_dropdown.users.is_opened()
        self.admin_page.menu.user_management_dropdown.users.search_user(fake.user_name())
