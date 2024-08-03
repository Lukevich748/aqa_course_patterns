import time

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ContactsPage(BasePage):

    _PAGE_URL = "https://release-crm.qa-playground.com/#/contacts"

    _NEW_CONTACT_BUTTON = "//a[@aria-label='New Contact']"
    _SAVE_BUTTON = "//button[@aria-label='Save']"
    _ELEMENT_CREATED_ALERT = "//div[text()='Element created']"

    _FIRST_NAME_FIELD = "//input[@id='first_name']"
    _LAST_NAME_FIELD = "//input[@id='last_name']"
    _TITLE_FIELD = "//input[@id='title']"
    _EMAIL_FIELD = "//input[@id='email']"

    def create_new_contact(self, first_name, last_name, title, email):
        self.wait.until(EC.element_to_be_clickable(self._NEW_CONTACT_BUTTON)).click()

        first_name_field = self.driver.find_element(*self._FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)
        assert first_name == first_name_field.get_attribute("value"), "First name field value does not match the expected input."

        last_name_field = self.driver.find_element(*self._LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)
        assert last_name == last_name_field.get_attribute("value"), "Last name field value does not match the expected input."

        title_field = self.driver.find_element(*self._TITLE_FIELD)
        title_field.send_keys(title)
        assert title == title_field.get_attribute("value"), "Title field value does not match the expected input."

        email_field = self.driver.find_element(*self._EMAIL_FIELD)
        email_field.send_keys(email)
        assert email == email_field.get_attribute("value"), "Email field value does not match the expected input."

        self.wait.until(EC.element_to_be_clickable(self._SAVE_BUTTON)).click()
        element_created_alert = self.wait.until(EC.visibility_of_element_located(self._ELEMENT_CREATED_ALERT))
        assert element_created_alert.is_displayed()