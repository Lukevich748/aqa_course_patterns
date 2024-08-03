from base.base_test import BaseTest


class TestContactsPage(BaseTest):

    def test_contacts_page(self):
        self.contacts_page.open()