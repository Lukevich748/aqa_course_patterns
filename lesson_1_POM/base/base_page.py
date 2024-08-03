from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lesson_1_POM.metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _CONTACTS_BUTTON = "//div[@class='MuiBox-root css-1t6c9ts']//a[text()='Contacts']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def open_contacts_tab(self):
        contacts_button = self.wait.until(EC.element_to_be_clickable(self._CONTACTS_BUTTON))
        contacts_button.click()
