import os
import pickle
import sys
import pytest
from selenium import webdriver
from base.base_test import LoginPage
from data.credentials import Credentials
from data.links import Links


@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--window-size=1920,1080")

    if os.environ["BROWSER"] == "chrome":
        driver = webdriver.Chrome(options=options)
        driver.get(Links.HOST)
        cookie_login(driver)
        request.cls.driver = driver
        yield
        driver.quit()

    elif os.environ["BROWSER"] == "firefox":
        driver = webdriver.Firefox(options=options)
        driver.get(Links.HOST)
        cookie_login(driver)
        request.cls.driver = driver
        yield
        driver.quit()


def cookie_login(driver):
    if os.path.exists("cookies.pkl"):
        driver.delete_all_cookies()

        with open("cookies.pkl", "rb") as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
    else:
        LoginPage(driver).enter_user_name(Credentials.LOGIN)
        LoginPage(driver).enter_password(Credentials.PASSWORD)
        LoginPage(driver).click_login_button()

        with open("cookies.pkl", "wb") as cookies_file:
            pickle.dump(driver.get_cookies(), cookies_file)


@pytest.fixture(autouse=True, scope="session")
def setup_allure_environment_properties():
    properties = {
        "Stage": os.environ["STAGE"],
        "Browser": os.environ["BROWSER"],
        "Python Version": f"{sys.version}"
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")