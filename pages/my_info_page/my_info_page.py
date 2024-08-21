from base.base_page import BasePage
from data.links import Links
from pages.my_info_page.components.my_info_menu import MyInfoMenu
from pages.my_info_page.components.personal_details import PersonalDetails


class MyInfoPage(BasePage):

    _PAGE_URL = Links.MY_INFO_PAGE

    @property
    def menu(self):
        self._menu = MyInfoMenu(self.driver)
        return self._menu

    @property
    def personal_details(self):
        return PersonalDetails(self.driver)