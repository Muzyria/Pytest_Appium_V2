import time

from base.base_test import BaseTest


class TestFirst(BaseTest):

    def test_try(self):
        self.login_page_syncwise360.open()
        self.login_page_syncwise360.is_opened()
        self.login_page_syncwise360.enter_login("")


        # self.login_page_syncwise360.enter_password("")
        # self.login_page_syncwise360.click_login_button()
        # self.login_page_syncwise360.spinner()
        time.sleep(5)

