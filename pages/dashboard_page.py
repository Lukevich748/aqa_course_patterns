import allure
from data.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    _PAGE_URL = Links.DASHBOARD_PAGE

    # Menu
    _MY_INFO_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='My Info']"

    @allure.step("Click on 'My Info' button")
    def click_my_info_button(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._MY_INFO_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"