from appium import webdriver

from test_app.test_wechat.page.app import app


class TestWework:
    def setup(self):
        self.app=app()
        self.main=self.app.start()


    def teardown(self):
        pass
        # self.driver.quit()
    def test_addcontact(self):
        self.main.goto_main().goto_contact().goto_addcontact().goto_editcontact().go_back().verif_toast()




