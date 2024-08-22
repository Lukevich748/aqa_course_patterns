import allure
from base.base_page import BasePage


class MyInfoMenu(BasePage):

    _PERSONAL_DETAILS_TAB = "//a[text()='Personal Details']"

    @allure.step("Open 'Personal Details' Tab")
    def open_personal_details(self):
        self.wait_element_to_be_clickable(self._PERSONAL_DETAILS_TAB)
        self.click(self._PERSONAL_DETAILS_TAB)
