from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CompaniesPage(BasePage):

    _PAGE_URL = "https://release-crm.qa-playground.com/#/companies"

    _NEW_COMPANY_BUTTON = "//a[@aria-label='New Company']"
    _SAVE_BUTTON = "//button[@aria-label='Save']"
    _ELEMENT_CREATED_ALERT = "//div[text()='Element created']"

    _COMPANY_NAME_FIELD = "//input[@id='name']"
    _CITY_FIELD = "//input[@id='city']"
    _PHONE_NUMBER_FIELD = "//input[@id='phone_number']"

    def create_new_company(self, company_name, city, phone_number):
        self.wait.until(EC.element_to_be_clickable(self._NEW_COMPANY_BUTTON)).click()
        assert self.driver.current_url == "https://release-crm.qa-playground.com/#/companies/create"

        company_name_field = self.driver.find_element(*self._COMPANY_NAME_FIELD)
        company_name_field.send_keys(company_name)
        assert company_name == company_name_field.get_attribute("value"), "Company name field value does not match the expected input."

        city_field = self.driver.find_element(*self._CITY_FIELD)
        city_field.send_keys(city)
        assert city == city_field.get_attribute("value"), "City field value does not match the expected input."

        phone_number_field = self.driver.find_element(*self._PHONE_NUMBER_FIELD)
        phone_number_field.send_keys(phone_number)
        assert phone_number == phone_number_field.get_attribute("value"), "Phone number field value does not match the expected input."

        self.wait.until(EC.element_to_be_clickable(self._SAVE_BUTTON)).click()
        element_created_alert = self.wait.until(EC.visibility_of_element_located(self._ELEMENT_CREATED_ALERT))
        assert element_created_alert.is_displayed()