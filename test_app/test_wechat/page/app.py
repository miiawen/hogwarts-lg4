#用于存放app相关的操作：启动app，关闭app，重启app，进入到主页
from appium import webdriver

from test_app.test_wechat.page.base import BasePage
from test_app.test_wechat.page.main_page import MainPage


class app(BasePage):
    def start(self):
        # 用if判断是否启动driver，如果没启动就初始化启动driver；已启动的话，就使用launch——app方法启动app
        if self.driver==None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps) #建立客户端与服务器的连接
            self.driver.implicitly_wait(5)
        else:
            #启动app，启动的页面是caps里面设置的activity
            self.driver.launch_app()
        return self
    def restart(self):
        pass
    def stop(self):
        self.driver.quit()
    def goto_main(self):
        return MainPage(self.driver)


