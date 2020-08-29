import unittest
import warnings
from time import sleep

from parameterized import parameterized

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page import Page
from tool.read_txt import read_txt


log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = GetDriver().get_driver()
        cls.page = Page(cls.driver)
        cls.page.page_home.click_login()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect_result, status):
        self.page.page_login.input_username(username)
        self.page.page_login.input_pwd(pwd)
        self.page.page_login.input_verify(verify_code)
        self.page.page_login.click_login()
        if status == "true":
            try:
                assert self.page.page_me.isexist_myshop()
            except Exception as e:
                log.error("错误：{}".format(e))
                self.page.page_home.get_image()

            self.page.page_me.click_quit()
            self.page.page_home.click_login()
        else:
            warn = self.page.page_login.get_warning_text()
            print(warn)
            try:
                assert warn == expect_result
            except Exception as e:
                log.error("错误：{}".format(e))
                self.page.page_home.get_image()

            self.page.page_login.click_warning()
