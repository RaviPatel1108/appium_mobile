from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from demo1_android.demo_app_install import AppiumConfig


class TestAndroidDeviceCloud(AppiumConfig):

    def test_invalid_sign_up_email_test(self):
        self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='First name']").send_keys("bala")
        self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Last name']").send_keys("bala")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").clear()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").send_keys("Aug")
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").send_keys(
            "20")
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys(
            "1995")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email address']").send_keys(
            "test123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']").send_keys("welcome123")

        # click on create
        # assert the error message of mail id
