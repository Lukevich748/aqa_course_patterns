from pages.login_page import LoginPage
from data.credentials import Credentials
from pages.my_info_page import MyInfoPage


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.my_info_page = MyInfoPage(self.driver)
