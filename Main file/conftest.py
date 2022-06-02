from appium import webdriver
import pytest
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="TELock"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption('--browser_name')
    if browser_name == "TELock":
        desired_cap = {
            "appium:deviceName": "moto g(6) plus",
            "platformName": "Android",
            "appium:app": "C:\\Users\\ELCOT\\Downloads\\app-debug_Apr_22_22.apk",
            "appium:platformVersion": "9",
            "ignoreHiddenApiPolicyError": "true"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    else:
        print("invalid")
    request.cls.driver = driver
    yield
    driver.quit()
