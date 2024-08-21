import allure
import platform
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _ADMIN_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='Admin']"
    _MY_INFO_BUTTON = "//ul[@class='oxd-main-menu']//span[text()='My Info']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self._PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def cmd_ctr_button(self):
        os_name = platform.system()
        cmd_ctrl_button = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL
        return cmd_ctrl_button

    # Sidebar menu
    @allure.step("Click on 'My Info' button")
    def click_my_info_button(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._MY_INFO_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"

    @allure.step("Click on 'Admin' button")
    def click_admin_button(self):
        my_info_button = self.wait.until(EC.element_to_be_clickable(self._ADMIN_BUTTON))
        my_info_button.click()
        assert self.driver.current_url != self._PAGE_URL, "The current URL is unexpectedly the same as the page URL"