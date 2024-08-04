from base.base_test import BaseTest
from faker import Faker

fake = Faker()


class TestDealsPage(BaseTest):

    def test_deals_page(self):
        self.deals_page.open()
        self.deals_page.create_new_deal(deal_name=fake.name(), amount=fake.random_digit())