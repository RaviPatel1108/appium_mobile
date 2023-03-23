from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "app": "bs://6f1fd39e5beae18971921e3f06ddd40bac1ee9ba",
    "platformVersion": "9.0",
    "deviceName": "Google Pixel 3",
    "bstack:options": {
        "projectName": "First Behave Android Project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",
        # Set your access credentials
        "userName": "ravipatel_ImV4Bk",
        "accessKey": "e5wyS7fEvx44kHQxJus3"
    }
}

driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()

print(driver.page_source)

driver.quit()
