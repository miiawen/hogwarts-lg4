#企业微信主页
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.test_wechat.page.base import BasePage
from test_app.test_wechat.page.contact_page import Contact


class MainPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def goto_contact(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/hp4']//*[2]").click()
        return Contact(self.driver)
