from base.base_test import BaseTest
from faker import Faker
fake = Faker()


class TestLoginPage(BaseTest):

    def test_login_page(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_user_name(self.credentials.LOGIN)
        self.login_page.enter_password(self.credentials.PASSWORD)
        self.login_page.click_login_button()

        self.my_info_page.open()
        self.my_info_page.is_opened()
        self.my_info_page.enter_first_name(fake.first_name())
        self.my_info_page.enter_last_name(fake.last_name())