#添加成员页面，可跳转到手动添加联系人页面
# from test_app.test_wechat.page.editcontact_page import EditContact
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.test_wechat.page.base import BasePage


class AddContact(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def goto_editcontact(self):
        from test_app.test_wechat.page.editcontact_page import EditContact
        self.driver.find_element_by_xpath(
        "//*[@resource-id='com.tencent.wework:id/d28']//*[@resource-id='com.tencent.wework:id/cox']").click()
        return EditContact(self.driver)
    def verif_toast(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result



