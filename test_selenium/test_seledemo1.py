import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Testdemo():

    def setup(self):
        browser=os.getenv('browser')
        if browser=='firefox':
            self.driver=webdriver.Firefox
        elif browser=='chrome':
            self.driver=webdriver.Chrome
        # option=webdriver.ChromeOptions()
        # option.add_experimental_option('w3c',False)
        # self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        # pass
        self.driver.quit()
    @pytest.mark.skip
    def test_seledemo1(self):
        self.driver.get('https://www.baidu.com')
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('霍格沃兹测试学院')
        ele=self.driver.find_element(By.XPATH,'//*[@id="u1"]//span')
        action=ActionChains(self.driver)
        action.move_to_element(ele)
        # cli=self.driver.find_element(By.XPATH,'//*[@id="s-user-setting-menu]/div/a')
        # action.move_to_element(cli).click()
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get('https://www.baidu.com')
        ele_click=self.driver.find_element(By.XPATH,'//*[@id="u1"]//a')
        # ele_doubleclick=self.driver.find_element(By.XPATH,'//*[@id=u1]//a')
        # ele_rightclick=self.driver.find_element(By.XPATH,'//*[@id=u1]//a')
        action=ActionChains(self.driver)
        action.click(ele_click)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_keys(self):
        self.driver.get('https://www.baidu.com')
        ele=self.driver.find_element(By.XPATH, '//*[@id="kw"]')
        ele.click()
        action=ActionChains(self.driver)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys('jreey').pause(2)
        action.perform()
    @pytest.mark.skip
    def test_touch_action(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element(By.XPATH, '//*[@id="kw"]')
        search=self.driver.find_element_by_id("su")
        ele.send_keys('selnium测试')
        action=TouchActions(self.driver)
        action.tap(search)
        sleep(3)
        action.scroll_from_element(ele,0,10000).perform()
        sleep(3)
#表单操作
    @pytest.mark.skip
    def test_form(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("18589026165")
        password=self.driver.find_element_by_id('TANGRAM__PSP_11__password')
        password.send_keys("w123456")
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(5)
    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # print(self.driver.current_window_handle)
        windows=self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("18589026165")
        password = self.driver.find_element_by_id('TANGRAM__PSP_11__password')
        password.send_keys("w123456")
        sleep(3)
