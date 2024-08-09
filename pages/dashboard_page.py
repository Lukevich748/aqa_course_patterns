import allure
from data.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    _PAGE_URL = Links.DASHBOARD_PAGE

    # Menu
    _ADMIN_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='Admin']"
    _MY_INFO_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='My Info']"

    _WIDGETS_LIST = "//div[@class='oxd-layout-context']//div[contains(@class, 'oxd-grid-item--gutters orangehrm-dashboard-widget')]"

    @allure.step("Click on 'My Info' button")
    def click_my_info_button(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._MY_INFO_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"

    @allure.step("Click on 'Admin' button")
    def click_admin_button(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._ADMIN_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"

    @allure.step("Check number of widgets")
    def check_widgets_number(self):
        widgets_list = self.wait.until(EC.visibility_of_all_elements_located(self._WIDGETS_LIST))
        assert len(widgets_list) == 7, f"Incorrect number of widgets: expected 7, but got {len(widgets_list)}"