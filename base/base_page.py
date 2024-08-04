from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _CONTACTS_BUTTON = "//div[@aria-label='Navigation Tabs']//a[text()='Contacts']"
    _COMPANIES_BUTTON = "//div[@aria-label='Navigation Tabs']//a[text()='Companies']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self._PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))