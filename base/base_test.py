from pages.contacts_page import ContactsPage
from pages.companies_page import CompaniesPage


class BaseTest:

    def setup_method(self):
        self.contacts_page = ContactsPage(self.driver)
        self.companies_page = CompaniesPage(self.driver)