import allure
from base.base_page import BasePage
from data.links import Links
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage(BasePage):

    _PAGE_URL = Links.MY_INFO_PAGE

    _FIRST_NAME_FIELD = "//input[@name='firstName']"
    _LAST_NAME_FIELD = "//input[@name='lastName']"

    _SAVE_BUTTON = "//div[@class='oxd-form-actions']/p/following-sibling::button"

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD))
        first_name_field.send_keys(self.cmd_ctr_button() + "A")
        first_name_field.send_keys(Keys.BACKSPACE)
        first_name_field.send_keys(first_name)
        assert first_name == first_name_field.get_attribute("value"), f"The firstname field does not contain '{first_name}'"

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        last_name_field = self.wait.until(EC.element_to_be_clickable(self._LAST_NAME_FIELD))
        last_name_field.send_keys(self.cmd_ctr_button() + "A")
        last_name_field.send_keys(Keys.BACKSPACE)
        last_name_field.send_keys(last_name)
        assert last_name == last_name_field.get_attribute("value"), f"The lastname field does not contain '{last_name}'"
