from appium import webdriver

desired_cap = {
    "appium:deviceName": "moto g(6) plus",
    "platformName": "Android",
    "appium:app": "C:\\Users\\ELCOT\\Downloads\\app-debug_Apr_22_22.apk",
    "appium:platformVersion": "9",
    "ignoreHiddenApiPolicyError": "true"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.find_element(By.ID, "com.telocks.te:id/ctaSigniIn").text
self.driver.find_elements(By.XPATH, "/android.widget.TextView[@id='android:id/tex1']")