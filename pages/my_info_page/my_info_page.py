from base.base_page import BasePage
from data.links import Links
from pages.my_info_page.components.my_info_menu import MyInfoMenu


class MyInfoPage(BasePage):

    _PAGE_URL = Links.MY_INFO_PAGE

    @property
    def menu(self):
        self_menu = MyInfoMenu(self.driver)
        return self_menu