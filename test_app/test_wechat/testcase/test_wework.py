from appium import webdriver
import appium
from appium.webdriver.common.mobileby import MobileBy


class TestWework:
    def setup(self):
        caps={}
        caps["platformName"]="android"
        caps["deviceName"]="127.0.0.1:7555"
        caps["appPackage"]="com.tencent.wework"
        caps["appActivity"]=".launch.WwMainActivity"
        caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_addstaff(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/hp4']//*[2]").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/baj']//*[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/d28']//*[@resource-id='com.tencent.wework:id/cox']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ba5']//*[@text='必填']").send_keys('zhangsan')
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/d5l']//*[@resource-id='com.tencent.wework:id/b5z']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/bls']//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys('13567886532')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result=="添加成功"

    def test_delete(self):
        pass











