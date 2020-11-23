import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWx:
    def setup(self):
        # 先cmd页面输入命令：chrome --remote-debugging-port=9222，启动chrome浏览器，再进行复用浏览器
        option = Options()
        option.debugger_address = "127.0.0.1:9222"#指定本地地址和cmd设置的端口号
        self.driver = webdriver.Chrome()

    def teardown(self):
        pass
        # self.driver.quit()

    def test_wx(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    # @pytest.mark.skip
    def test_cookie(self):
        # 在复用浏览器打开想要复用的页面后，使用get_cookies()方法获取cookies
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1606118009, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853973611691'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'L5NR36gc4pitmSOkfBiLtNc5e2mliBwNoteyMW3ZAPWJ-7E2iubmXK8UEewP4IKo4nidSbvpyfUijOOj4QT5Ngk8wneqFX1Uvkcw7WRzuXbjRX-u-Z3EKLvFx0uMvd6W_XHr29Xki3SoOvQmWj8qFfhZxl6mH5FjB7YaAJRZPDJ87o3a7YTqzPtwjq5iK2oWDAF0s6J9YHFHpoRKWEbEJty0v0Nuc23iDsc35_VONRAKCQj6qwuBZtEOngBA4fg9cFtSmuVdAjGPCW5hL-TONw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'Sr77A67VI9tPIl6jfZ0cCNJajB7xVnyNxt4LbY8Dy_Sm2SrKiu90dtHcaBtlFOMu'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2946919'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324968192742'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853973611691'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637480333, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1605943369,1605943518,1605943607,1605944334'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '6277919852691854'},
            {'domain': '.qq.com', 'expiry': 1606204349, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1646466631.1606039865'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1606146898, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '6pf9cjq'},
            {'domain': '.qq.com', 'expiry': 1669189949, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.292972274.1605934739'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1637470562, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1608709949, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        # print(cookies)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(3)
        # 使用for循环，将列表内的字典元素读取出来
        for cookie in cookies:
            # 防止有效期的格式出现小数点等非法报错，采用if语句进行判断，若有异常，就删除这个元素
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
                # print(cookie)
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)
