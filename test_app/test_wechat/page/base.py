#用于存放driver的初始化
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver
