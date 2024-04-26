import time

from base.base_test import BaseTest


class TestFirst(BaseTest):

    def test_try(self):
        self.login_page_control.open()
        self.login_page_control.is_opened()
        self.login_page_control.enter_login("123")
        self.login_page_control.enter_password("123")
        self.login_page_control.click_login_button()
        time.sleep(3)

