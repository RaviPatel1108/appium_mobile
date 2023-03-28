import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

""" long press"""


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"D:\Python_Trainning_Material\khan-academy-7-3-2.apk",
            "noReset": True
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAdvanceCode(AppiumConfig):
    def test_tap_using_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        action = TouchAction(self.driver)
        action.tap(x=900, y=900, count=5).perform()
        time.sleep(5)