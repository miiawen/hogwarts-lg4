import appium
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestXueqiu:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='android'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']=' com.xueqiu.android'
        desired_caps['appActivity']='.common.MainActivity'
        desired_caps['noReset']='true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass
        # self.driver.quit()

    def test_xq(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price=float(self.driver.find_element_by_xpath("//*[@text='BABA']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        # locator=self.driver.find_element(MobileBy.XPATH,("//*[@text='BABA']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']"))
        # WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located(locator))
        assert current_price>200


        self.driver.back()
        self.driver.back()





