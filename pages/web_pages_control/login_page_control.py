from base.base_page import BasePage
from config.links import Links_control
from selenium.webdriver.support import expected_conditions as EC


class LoginPageControl(BasePage):

    PAGE_URL = Links_control.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@id='btn-submit']")

    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys("")

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys("")

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_LOGIN)).click()
