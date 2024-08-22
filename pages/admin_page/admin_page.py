from base.base_page import BasePage
from data.links import Links
from pages.admin_page.components.admin_top_bar_menu import AdminTopBarMenu
from pages.admin_page.components.nationalities import Nationalities


class AdminPage(BasePage):

    _PAGE_URL = Links.ADMIN_PAGE

    @property
    def menu(self):
        return AdminTopBarMenu(self.driver)

    @property
    def nationalities(self):
        return Nationalities(self.driver)
