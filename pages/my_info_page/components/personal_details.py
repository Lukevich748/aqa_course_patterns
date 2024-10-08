import allure
from selenium.webdriver import Keys
from base.base_page import BasePage


class PersonalDetails(BasePage):

    _FIRST_NAME_FIELD = "//input[@name='firstName']"
    _MIDDLE_NAME_FIELD = "//input[@name='middleName']"
    _LAST_NAME_FIELD = "//input[@name='lastName']"

    _SAVE_BUTTON = "//div[@class='oxd-form-actions']/p/following-sibling::button"
    _SUCCESS_ALERT = "//div[@aria-live='assertive']"

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        self.wait_element_to_be_clickable(self._FIRST_NAME_FIELD)
        self.fill(self._FIRST_NAME_FIELD, self.cmd_ctr_button + "A")
        self.fill(self._FIRST_NAME_FIELD, Keys.BACKSPACE)
        self.fill(self._FIRST_NAME_FIELD, first_name)
        assert first_name == self.find(self._FIRST_NAME_FIELD).get_attribute("value"), f"The first name field does not contain '{first_name}'"

    @allure.step("Enter middle name")
    def enter_middle_name(self, middle_name):
        self.wait_element_to_be_clickable(self._MIDDLE_NAME_FIELD)
        self.fill(self._MIDDLE_NAME_FIELD, self.cmd_ctr_button + "A")
        self.fill(self._MIDDLE_NAME_FIELD, Keys.BACKSPACE)
        self.fill(self._MIDDLE_NAME_FIELD, middle_name)
        assert middle_name == self.find(self._MIDDLE_NAME_FIELD).get_attribute("value"), f"The middle name field does not contain '{middle_name}'"

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        self.wait_element_to_be_clickable(self._LAST_NAME_FIELD)
        self.fill(self._LAST_NAME_FIELD, self.cmd_ctr_button + "A")
        self.fill(self._LAST_NAME_FIELD, Keys.BACKSPACE)
        self.fill(self._LAST_NAME_FIELD, last_name)
        assert last_name == self.find(self._LAST_NAME_FIELD).get_attribute("value"), f"The last name field does not contain '{last_name}'"

    @allure.step("Click on 'Save' button")
    def click_save_button(self):
        self.wait_element_to_be_clickable(self._SAVE_BUTTON)
        self.click(self._SAVE_BUTTON)
        assert self.wait_visibility_of_element(self._SUCCESS_ALERT, message="Success alert is not visible")
        assert self.wait_invisibility_of_element(self._SUCCESS_ALERT, message="Success alert is visible")