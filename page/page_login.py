from selenium.webdriver.common.by import By

from base.base import Base


class PageLogin(Base):

    login_username = By.CSS_SELECTOR, "#username"
    login_pwd = By.CSS_SELECTOR, "#password"
    login_verify = By.CSS_SELECTOR, "#verify_code"
    login_btn = By.CSS_SELECTOR, ".J-login-submit"
    warning_text = By.CSS_SELECTOR, ".layui-layer-content"
    warning_define = By.CSS_SELECTOR, ".layui-layer-btn0"

    def input_username(self, username):
        self.base_input(self.login_username, username)

    def input_pwd(self, pwd):
        self.base_input(self.login_pwd, pwd)

    def input_verify(self, verify):
        self.base_input(self.login_verify, verify)

    def click_login(self):
        self.base_click(self.login_btn)

    def get_warning_text(self):
        return self.base_get_text(self.warning_text)

    def click_warning(self):
        self.base_click(self.warning_define)

    def login(self):
        self.input_username("13800001111")
        self.input_pwd("123456")
        self.input_verify("8888")
        self.click_login()

