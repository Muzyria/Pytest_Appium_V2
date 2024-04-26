import pytest

from pages.web_pages_control.login_page_control import LoginPageControl
from pages.web_pages_syncwise360.login_page_syncwise360 import LoginPageSyncwise360


class BaseTest:
    login_page_control: LoginPageControl

    login_page_syncwise360: LoginPageSyncwise360

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page_control = LoginPageControl(driver)

        request.cls.login_page_syncwise360 = LoginPageSyncwise360(driver)


