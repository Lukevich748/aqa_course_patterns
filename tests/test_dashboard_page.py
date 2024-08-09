import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest
from faker import Faker

fake = Faker()


@allure.epic("Dashboard Management")
@allure.feature("Dashboard Widget Management")
@allure.story("Check Widgets Number")
class TestDashboardPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.title("Check the Number of Widgets on the Dashboard")
    def test_check_widgets_number(self):
        self.dashboard_page.is_opened()
        self.dashboard_page.check_widgets_number()
