import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class PersonalDetails(BasePage):

    _FIRST_NAME_FIELD = "//input[@name='firstName']"
    _MIDDLE_NAME_FIELD = "//input[@name='middleName']"
    _LAST_NAME_FIELD = "//input[@name='lastName']"

    _SAVE_BUTTON = "//div[@class='oxd-form-actions']/p/following-sibling::button"
    _SUCCESS_ALERT = "//div[@aria-live='assertive']"

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD))
        first_name_field.send_keys(self.cmd_ctr_button() + "A")
        first_name_field.send_keys(Keys.BACKSPACE)
        first_name_field.send_keys(first_name)
        assert first_name == first_name_field.get_attribute("value"), f"The first name field does not contain '{first_name}'"

    @allure.step("Enter middle name")
    def enter_middle_name(self, middle_name):
        middle_name_field = self.wait.until(EC.element_to_be_clickable(self._MIDDLE_NAME_FIELD))
        middle_name_field.send_keys(self.cmd_ctr_button() + "A")
        middle_name_field.send_keys(Keys.BACKSPACE)
        middle_name_field.send_keys(middle_name)
        assert middle_name == middle_name_field.get_attribute("value"), f"The middle name field does not contain '{middle_name}'"

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        last_name_field = self.wait.until(EC.element_to_be_clickable(self._LAST_NAME_FIELD))
        last_name_field.send_keys(self.cmd_ctr_button() + "A")
        last_name_field.send_keys(Keys.BACKSPACE)
        last_name_field.send_keys(last_name)
        assert last_name == last_name_field.get_attribute("value"), f"The last name field does not contain '{last_name}'"

    @allure.step("Click on 'Save' button")
    def click_save_button(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self._SAVE_BUTTON))
        save_button.click()
        assert self.wait.until(EC.visibility_of_element_located(self._SUCCESS_ALERT)), "Success alert is not visible"
        assert self.wait.until(EC.invisibility_of_element_located(self._SUCCESS_ALERT)), "Success alert is visible"