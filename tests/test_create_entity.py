from base.base_test import BaseTest
from faker import Faker

fake = Faker()


class TestCreateEntity(BaseTest):

    def test_create_entity(self):
        self.contacts_page.open()
        self.contacts_page.is_opened()
        self.contacts_page.create_new_contact(first_name=fake.first_name(), last_name=fake.last_name(), title=fake.city(), email=fake.email())
        self.companies_page.open()
        self.companies_page.is_opened()
        self.companies_page.create_new_company(company_name=fake.company(), city=fake.city(), phone_number=fake.phone_number())
        self.deals_page.open()
        self.deals_page.is_opened()
        self.deals_page.create_new_deal(deal_name=fake.name(), amount=fake.random_digit())
        self.base_page.reset_db()