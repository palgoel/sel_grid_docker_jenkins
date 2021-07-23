# Run Selenium tests in parallel with Python for Selenium Python tutorial
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import boto3
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

def pytest_addoption(parser):
    parser.addoption(
        "--testBrowser",
        action="store",
        default = "chrome",
        help="supply the browser where test needs to run",
    )
@pytest.fixture(scope="session")
def driver_browser(request):
    browser= request.config.getoption("--testBrowser")
    print("Browser thru cmd =", browser)
    if browser == "firefox":
        web_driver = webdriver.Remote("http://192.168.1.30:4444/wd/hub", DesiredCapabilities.FIREFOX)
    else:
        web_driver = webdriver.Remote("http://192.168.1.30:4444/wd/hub", DesiredCapabilities.CHROME)
    return web_driver

@pytest.fixture(scope="class")
def driver_init(request,driver_browser):
    driver_browser.implicitly_wait(10)
    driver_browser.get("http://www.google.com")
    request.cls.driver = driver_browser
    yield
    driver_browser.quit()

@pytest.fixture(scope="class")
def driver_init_chrome(request):
    driver = webdriver.Remote("http://192.168.1.30:4444/wd/hub", DesiredCapabilities.CHROME)
    driver.get("http://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def driver_init_firefox(request):
    driver = webdriver.Remote("http://192.168.1.30:4444/wd/hub", DesiredCapabilities.FIREFOX)
    driver.get("http://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()
