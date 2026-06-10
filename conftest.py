import pytest
from selenium import webdriver
from datetime import datetime
def pytest_addoption(parser):
        parser.addoption(
            "--browser_name", action="store", default="chrome", help="run slow tests"
        )
@pytest.fixture(scope="function")
def driver(request):
    browser= request.config.getoption("--browser_name")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox() 
    driver.maximize_window()   
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        driver.save_screenshot(
            f"Screenshots/{item.name}_{timestamp}.png"
        )
