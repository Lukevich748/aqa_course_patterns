import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from data.links import Links


class Users(BasePage):

    _PAGE_URL = Links.ADMIN_PAGE

    _USER_NAME_FIELD = "//div[@class='oxd-table-filter']//input[contains(@class, 'input')]"
    _SEARCH_BUTTON = "//button[@type='submit']"

    def search_user(self, user_name):
        with allure.step(f"Search '{user_name}' user"):
            self.wait_element_to_be_clickable(self._USER_NAME_FIELD)
            self.fill(self._USER_NAME_FIELD, self.cmd_ctr_button + "A")
            self.fill(self._USER_NAME_FIELD, Keys.BACKSPACE)
            self.fill(self._USER_NAME_FIELD, user_name)
            assert user_name == self.find(self._USER_NAME_FIELD).get_attribute("value"), f"The user name field does not contain '{user_name}'"