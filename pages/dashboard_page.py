import allure
from data.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    _PAGE_URL = Links.DASHBOARD_PAGE

    _WIDGETS_LIST = "//div[@class='oxd-layout-context']//div[contains(@class, 'oxd-grid-item--gutters orangehrm-dashboard-widget')]"

    @allure.step("Check number of widgets")
    def check_widgets_number(self):
        widgets_list = self.wait.until(EC.visibility_of_all_elements_located(self._WIDGETS_LIST))
        assert len(widgets_list) == 7, f"Incorrect number of widgets: expected 7, but got {len(widgets_list)}"