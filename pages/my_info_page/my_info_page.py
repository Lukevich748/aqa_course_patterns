import allure
from base.base_page import BasePage
from data.links import Links
from pages.my_info_page.components.personal_details import PersonalDetails


class MyInfoPage(BasePage):

    _PAGE_URL = Links.MY_INFO_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.personal_details = PersonalDetails(self.driver)

    @allure.step("Open 'Personal Details' Tab")
    def open_personal_details(self):
        self.click(self._PERSONAL_DETAILS_TAB)