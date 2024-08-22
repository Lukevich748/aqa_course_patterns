import allure
from selenium.webdriver import Keys
from base.base_page import BasePage


class Nationalities(BasePage):

    _ADD_NATIONALITY_BUTTON = "//button[text()=' Add ']"

    _NATIONALITY_NAME_FIELD = "//div[@class='oxd-form-row']//input"
    _SAVE_BUTTON = "//button[text()=' Save ']"
    _SUCCESS_ALERT = "//div[@aria-live='assertive']"

    @allure.step("Click on 'Add' button")
    def click_add_nationality_button(self):
        self.wait_element_to_be_clickable(self._ADD_NATIONALITY_BUTTON)
        self.click(self._ADD_NATIONALITY_BUTTON)

    @allure.step("Click on 'Save' button")
    def click_save_button(self):
        self.wait_element_to_be_clickable(self._SAVE_BUTTON)
        self.click(self._SAVE_BUTTON)
        assert self.wait_visibility_of_elements(self._SUCCESS_ALERT, message="Success alert is not visible")
        assert self.wait_invisibility_of_element(self._SUCCESS_ALERT, message="Success alert is visible")

    @allure.step("Enter nationality name")
    def enter_nationality_name(self, nationality_name):
        self.wait_element_to_be_clickable(self._NATIONALITY_NAME_FIELD)
        self.fill(self._NATIONALITY_NAME_FIELD, self.cmd_ctr_button + "A")
        self.fill(self._NATIONALITY_NAME_FIELD, Keys.BACKSPACE)
        self.fill(self._NATIONALITY_NAME_FIELD, nationality_name)
        assert nationality_name == self.find(self._NATIONALITY_NAME_FIELD).get_attribute("value"), f"The nationality name field does not contain '{nationality_name}'"