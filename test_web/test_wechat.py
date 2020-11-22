import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWx:
    def setup(self):
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        pass
        # self.driver.quit()

    @pytest.mark.skip
    def test_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    # @pytest.mark.skip
    def test_cookie(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '17405973611148380'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1606071883, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5eu1nqi'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1637576347, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1608632348, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        # print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if 'expiry' in cookie.keys():
             cookie.pop('expiry')
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    @pytest.mark.skip
    def test_import_contacts(self):
        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
