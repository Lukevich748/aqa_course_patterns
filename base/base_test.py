from base.base_page import BasePage
from pages.contacts_page import ContactsPage
from pages.companies_page import CompaniesPage
from pages.deals_page import DealsPage


class BaseTest:

    def setup_method(self):
        self.base_page = BasePage(self.driver)
        self.contacts_page = ContactsPage(self.driver)
        self.companies_page = CompaniesPage(self.driver)
        self.deals_page = DealsPage(self.driver)