# Run Selenium tests in parallel with Python for Selenium Python tutorial
import pytest
from selenium import webdriver
import os
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import boto3
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

# os.environ['HUB_HOST'] = 'localhost'
# os.environ['BROWSER'] = 'chrome'

def pytest_addoption(parser):
    parser.addoption(
        "--testBrowser",
        action="store",
        default = "chrome",
        help="supply the browser where test needs to run",
    )
    parser.addoption(
        "--hubHost",
        action="store",
        default = "localhost",
        help="supply hub host",
    )

    ### below commented lines ate used to add markers to run tests, the value to be given from cmd to tell which tests to run###
    # parser.addoption(
    #     "--testCustomMarker",
    #     action="store",
    #     metavar="NAME",
    #     default="chrome",
    #     help="only run tests matching the environment NAME.",
    # )
# def pytest_configure(config):
#     # register an additional marker
#     config.addinivalue_line(
#         "markers", "env(name): mark test to run only on named environment"
#     )
#
# def pytest_runtest_setup(item):
#     envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
#     if envnames:
#         if item.config.getoption("--testCustomMarker") not in envnames:
#             pytest.skip("test requires env in {!r}".format(envnames))\

@pytest.fixture(scope="session")
def driver_browser(request):
    browser= os.environ['BROWSER']
    print("Browser thru cmd =", browser)
    if browser == "firefox":
        web_driver = webdriver.Remote("http://"+os.environ['HUB_HOST']+":4444/wd/hub", DesiredCapabilities.FIREFOX)
    else:
        web_driver = webdriver.Remote("http://"+os.environ['HUB_HOST']+":4444/wd/hub", DesiredCapabilities.CHROME)
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
    driver = webdriver.Remote("http://"+os.environ['HUB_HOST']+":4444/wd/hub", DesiredCapabilities.CHROME)
    driver.get("http://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def driver_init_firefox(request):
    driver = webdriver.Remote("http://"+os.environ['HUB_HOST']+":4444/wd/hub", DesiredCapabilities.FIREFOX)
    driver.get("http://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()
