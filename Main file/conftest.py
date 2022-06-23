from appium import webdriver
import pytest
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--name", action="store", default="karpagaraj"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    name = request.config.getoption('--name')
    if name == "Karpagaraj":
        desired_cap = {
            "appium:deviceName": "moto g(6) plus",
            "platformName": "Android",
            "appium:app": "D:\\Telock\\app-debug_Apr_3_22.apk",
            "appium:platformVersion": "9",
            "ignoreHiddenApiPolicyError": "true"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    elif name == "Alex":
        desired_cap = {
             "appium:deviceName": "Emulator",
             "platformName": "Android",
             "appium:app": "G:\\thirdeye\\drivers\\app-debug_Apr_22_22.apk",
             "appium:platformVersion": "11",
             "appium:ignoreHiddenApiPolicyError": "true"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    else:
        print("invalid")
    request.cls.driver = driver
    yield
    driver.quit()
