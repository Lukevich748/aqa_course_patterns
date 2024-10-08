import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest
from faker import Faker

fake = Faker()


@allure.epic("Employee Personal Data Management")
class TestMyInfoPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Editing Employee Personal Details")
    @allure.story("Edit Employee Full Name")
    def test_edit_employee_full_name(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.successful_login()
        self.dashboard_page.is_opened()
        self.dashboard_page.open_my_info_tab()
        self.my_info_page.is_opened()
        self.my_info_page.personal_details.enter_first_name(fake.first_name())
        self.my_info_page.personal_details.enter_middle_name(fake.name())
        self.my_info_page.personal_details.enter_last_name(fake.last_name())
        self.my_info_page.personal_details.click_save_button()