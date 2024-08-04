import random
from selenium.webdriver import Keys
import platform
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class DealsPage(BasePage):

    _PAGE_URL = "https://release-crm.qa-playground.com/#/deals"

    _NEW_DEAL_BUTTON = "//a[@aria-label='New Deal']"
    _SAVE_BUTTON = "//button[@aria-label='Save']"

    _DEAL_NAME_FIELD = "//input[@id='name']"
    _COMPANY_FIELD = "//input[@id='company_id']"
    _COMPANIES_LIST = "//ul[@id='company_id-listbox']/li"
    _AMOUNT_FIELD = "//input[@id='amount']"

    def choose_random_company(self):
        company_field = self.driver.find_element(*self._COMPANY_FIELD)
        company_field.click()
        companies_list = [company for company in self.wait.until(EC.visibility_of_all_elements_located(self._COMPANIES_LIST))]
        company = random.choice(companies_list)
        company.click()

    def create_new_deal(self, deal_name, amount):
        self.wait.until(EC.element_to_be_clickable(self._NEW_DEAL_BUTTON)).click()
        assert self.driver.current_url == "https://release-crm.qa-playground.com/#/deals/create"

        deal_name_field = self.driver.find_element(*self._DEAL_NAME_FIELD)
        deal_name_field.send_keys(deal_name)
        assert deal_name == deal_name_field.get_attribute("value"), "Deal name field value does not match the expected input."

        self.choose_random_company()

        os_name = platform.system()
        CMD_CTRL = Keys.COMMAND if os_name == "darwin" else Keys.CONTROL

        amount_field = self.driver.find_element(*self._AMOUNT_FIELD)
        amount_field.send_keys(CMD_CTRL + "A")
        amount_field.send_keys(Keys.BACKSPACE)
        amount_field.send_keys(amount)
        assert amount == amount_field.get_attribute("value"), "Amount field value does not match the expected input."
