#通讯录页面
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.test_wechat.page.addcontact_page import  AddContact
from test_app.test_wechat.page.base import BasePage


class Contact(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def goto_addcontact(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/baj']//*[@text='添加成员']").click()
        return AddContact(self.driver)
