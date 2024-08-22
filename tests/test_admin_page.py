import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest
from faker import Faker

fake = Faker()


@allure.epic("System Administration")
@allure.feature("Nationality Management")
@allure.story("Add Nationality")
class TestAdminPage(BaseTest):

    @pytest.mark.smoker
    @allure.severity(Severity.NORMAL)
    @allure.title("Add a New Nationality")
    def test_add_nationality(self):
        self.dashboard_page.is_opened()
        self.dashboard_page.open_admin_tab()
        self.admin_page.is_opened()
        self.admin_page.menu.open_nationalities()
        self.admin_page.nationalities.click_add_nationality_button()
        self.admin_page.nationalities.enter_nationality_name(fake.country())
        self.admin_page.nationalities.click_save_button()