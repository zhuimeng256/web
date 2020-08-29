import unittest
import warnings
from time import sleep

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page import Page

log = GetLogger().get_logger()


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = GetDriver().get_driver()
        cls.page = Page(cls.driver)
        cls.page.page_home.click_login()
        cls.page.page_login.login()
        cls.page.page_me.click_home()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

    def test_cart(self):
        self.page.page_home.input("小米")
        self.page.page_home.click_search()
        self.page.page_shoplist.click_shoplist()
        self.page.page_shopdetail.click_joincard()
        self.page.page_shopdetail.switch_frame()
        try:
            assert self.page.page_shopdetail.sucess_join_text() == "添加成功"
        except Exception as e:
            log.error("错误：{}".format(e))
            self.page.page_home.get_image()
        self.page.page_shopdetail.switch_default()
        self.page.page_shopdetail.click_close()
        self.page.page_shopdetail.click_gocart()
        try:
            assert self.page.page_shopcart.isexist_settment()
        except Exception as e:
            log.error("错误：{}".format(e))
            self.page.page_home.get_image()


