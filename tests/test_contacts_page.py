import time

from base.base_test import BaseTest
from faker import Faker

fake = Faker()


class TestContactsPage(BaseTest):

    def test_contacts_page(self):
        self.contacts_page.open()
        self.contacts_page.create_new_contact(fake.first_name(), fake.last_name(), fake.city(), fake.email())
        self.companies_page.open()
        self.companies_page.is_opened()
        time.sleep(3)