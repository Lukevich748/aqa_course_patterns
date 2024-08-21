import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MyInfoMenu(BasePage):

    _PERSONAL_DETAILS_TAB = "//a[text()='Personal Details']"

    @allure.step("Open 'Personal Details' Tab")
    def open_personal_details(self):
        personal_details_tab = self.wait.until(EC.element_to_be_clickable(self._PERSONAL_DETAILS_TAB))
        personal_details_tab.click()
