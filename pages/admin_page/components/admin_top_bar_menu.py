import allure
from base.base_page import BasePage


class AdminTopBarMenu(BasePage):

    _JOB_TAB = "//nav[@aria-label='Topbar Menu']//span[text()='Job ']"
    _NATIONALITIES_TAB = "//nav[@aria-label='Topbar Menu']//a[text()='Nationalities']"

    @allure.step("Open 'Job' Tab")
    def job_dropdown(self):
        self.wait_element_to_be_clickable(self._JOB_TAB)
        self.click(self._JOB_TAB)

    @allure.step("Open 'Nationalities' Tab")
    def open_nationalities(self):
        self.wait_element_to_be_clickable(self._NATIONALITIES_TAB)
        self.click(self._NATIONALITIES_TAB)