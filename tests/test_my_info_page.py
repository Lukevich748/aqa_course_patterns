import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest
from faker import Faker

fake = Faker()


@allure.epic("Employee Personal Data Management")
@allure.feature("Editing Employee Personal Details")
@allure.story("Edit Employee Full Name")
class TestMyInfoPage(BaseTest):

    @pytest.mark.smoker
    @allure.severity(Severity.CRITICAL)
    @allure.title("Edit Employee Full Name on 'My Info Page'")
    def test_edit_employee_full_name(self):
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_button()
        self.my_info_page.is_opened()
        self.my_info_page.menu.open_personal_details()
        self.my_info_page.enter_first_name(fake.first_name())
        self.my_info_page.enter_middle_name(fake.name())
        self.my_info_page.enter_last_name(fake.last_name())
        self.my_info_page.click_save_button()