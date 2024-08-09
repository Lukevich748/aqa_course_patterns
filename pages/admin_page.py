import allure
from base.base_page import BasePage
from data.links import Links
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):

    _PAGE_URL = Links.ADMIN_PAGE

    _NATIONALITIES_TAB_BUTTON = "//nav[@aria-label='Topbar Menu']//a[text()='Nationalities']"
    _ADD_NATIONALITY_BUTTON = "//button[text()=' Add ']"

    _NATIONALITY_NAME_FIELD = "//div[@class='oxd-form-row']//input"
    _SAVE_BUTTON = "//button[text()=' Save ']"
    _SUCCESS_ALERT = "//div[@aria-live='assertive']"

    @allure.step("Click on 'Nationalities' button")
    def click_nationalities_tab_button(self):
        nationalities_tab_button = self.wait.until(EC.element_to_be_clickable(self._NATIONALITIES_TAB_BUTTON))
        nationalities_tab_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"

    @allure.step("Click on 'Add' button")
    def click_add_nationality_button(self):
        add_nationality_button = self.wait.until(EC.element_to_be_clickable(self._ADD_NATIONALITY_BUTTON))
        add_nationality_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"

    @allure.step("Click on 'Save' button")
    def click_save_button(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self._SAVE_BUTTON))
        save_button.click()
        assert self.wait.until(EC.visibility_of_element_located(self._SUCCESS_ALERT)), "Success alert is not visible"

    @allure.step("Enter nationality name")
    def enter_nationality_name(self, nationality_name):
        nationality_name_field = self.wait.until(EC.element_to_be_clickable(self._NATIONALITY_NAME_FIELD))
        nationality_name_field.send_keys(self.cmd_ctr_button() + "A")
        nationality_name_field.send_keys(Keys.BACKSPACE)
        nationality_name_field.send_keys(nationality_name)
        assert nationality_name == nationality_name_field.get_attribute("value"), f"The nationality name field does not contain '{nationality_name}'"