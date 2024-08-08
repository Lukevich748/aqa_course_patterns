import os
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--window-size=1920,1080")

    if os.environ["BROWSER"] == "chrome":
        driver = webdriver.Chrome(options=options)
        request.cls.driver = driver
        yield
        driver.quit()

    elif os.environ["BROWSER"] == "firefox":
        driver = webdriver.Firefox(options=options)
        request.cls.driver = driver
        yield
        driver.quit()