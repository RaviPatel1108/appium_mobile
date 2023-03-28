import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://4c2cbab03a154fbddd3fccb1c9e098ec4362cdd8",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "ravipatel_ImV4Bk",
                "accessKey": "e5wyS7fEvx44kHQxJus3",
                "projectName": "First Python project",
                "buildName": "bs://4c2cbab03a154fbddd3fccb1c9e098ec4362cdd8",
                "sessionName": "BStack first_test-ios"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestSampleApp(AppiumIosConfig):
    def test_text_box(self):
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="test-Username"]').send_keys("John")
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@name="test-Password"]').send_keys("John123")
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="test-LOGIN"]').click()
        actual_text = self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Username and password do not match any user in this service."]').text
        assert_that('Username and password do not match any user in this service.').is_equal_to(actual_text)