from pages.admin_page.admin_page import AdminPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from data.credentials import Credentials
from pages.my_info_page.my_info_page import MyInfoPage


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.admin_page = AdminPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.my_info_page = MyInfoPage(self.driver)
