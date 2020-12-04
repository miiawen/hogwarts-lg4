#编辑联系人信息页面
# from test_app.test_wechat.page.addcontact_page import AddContact
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.test_wechat.page.base import BasePage


class EditContact(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def go_back(self):
        from test_app.test_wechat.page.addcontact_page import AddContact
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ba5']//*[@text='必填']").send_keys(
            'tom')
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/d5l']//*[@resource-id='com.tencent.wework:id/b5z']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/bls']//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys('16754252778')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        return AddContact(self.driver)

