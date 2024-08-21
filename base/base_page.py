import allure
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_locator import MetaLocator
from helpers.ui_helper import UIHelper


class BasePage(UIHelper, metaclass=MetaLocator):

    _ADMIN_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='Admin']"
    _MY_INFO_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='My Info']"

    # Sidebar menu
    @allure.step("Open 'My Info' tab")
    def open_my_info_tab(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._MY_INFO_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"

    @allure.step("Open 'Admin' tab")
    def open_admin_tab(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._ADMIN_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"