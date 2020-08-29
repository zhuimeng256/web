import unittest
import warnings
from time import sleep

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page import Page

log = GetLogger().get_logger()

class TestOrder(unittest.TestCase):


    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = GetDriver().get_driver()
        self.page = Page(self.driver)
        self.page.page_home.click_login()
        self.page.page_login.login()
        self.page.page_me.click_home()

        self.page.page_home.input("小米")
        self.page.page_home.click_search()
        self.page.page_shoplist.click_shoplist()
        self.page.page_shopdetail.click_joincard()
        self.page.page_shopdetail.switch_frame()
        self.page.page_shopdetail.switch_default()
        self.page.page_shopdetail.click_close()
        self.page.page_shopdetail.click_gohome()

    def tearDown(self):
        GetDriver().quit_driver()

    def test_inorder(self):
        self.page.page_home.click_cart()
        self.page.page_shopcart.click_select()
        self.page.page_shopcart.click_settment()
        self.page.page_verify_order.find()
        self.page.page_verify_order.click_submit_order()
        try:
            assert self.page.page_sucess_order.get_text_cost() == "订单提交成功，请您尽快付款！"
        except Exception as e:
            log.error("错误：{}".format(e))
            self.page.page_home.get_image()


    def test_cost(self):
        self.page.page_home.click_myorder()
        self.page.page_myorder.switch_me()
        self.page.page_myorder.click_wait_cost()
        self.page.page_myorder.click_instance_cost()
        self.page.page_sucess_order.switch_me()
        self.page.page_sucess_order.click_goods_arrived()
        self.page.page_sucess_order.click_confirm_cost()
        try:
            assert self.page.page_sucess_order.get_text_cost() == "订单提交成功，我们将在第一时间给你发货！"
        except Exception as e:
            log.error("错误：{}".format(e))
            self.page.page_home.get_image()

