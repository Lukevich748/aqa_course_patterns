from base.base_test import BaseTest
from faker import Faker

fake = Faker()


class TestMyInfoPage(BaseTest):

    def test_my_info_page(self):
        self.my_info_page.open()
        self.my_info_page.is_opened()
        self.my_info_page.enter_first_name(fake.first_name())
        self.my_info_page.enter_last_name(fake.last_name())
        time.sleep(3)