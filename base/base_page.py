from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _CONTACTS_BUTTON = "//div[@aria-label='Navigation Tabs']//a[text()='Contacts']"
    _COMPANIES_BUTTON = "//div[@aria-label='Navigation Tabs']//a[text()='Companies']"
    _RESET_DB_BUTTON = "//button[@aria-label='Reset DB']"
    _RESET_DB_CONFIRM_BUTTON = "//button[contains(@class, 'confirm')]"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self._PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def reset_db(self):
        reset_db_button = self.wait.until(EC.element_to_be_clickable(self._RESET_DB_BUTTON))
        reset_db_button.click()
        self.wait.until(EC.visibility_of_element_located(self._RESET_DB_CONFIRM_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self._RESET_DB_CONFIRM_BUTTON)).click()