from lesson_1_POM.pages.contacts_page import ContactsPage


class BaseTest:

    def setup_method(self):
        self.contacts_page = ContactsPage(self.driver)