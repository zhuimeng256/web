from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_me import PageMe
from page.page_myorder import PageMyorder
from page.page_shopcart import PageShopcart
from page.page_shopdetail import PageShopdetail
from page.page_shoplist import PageShoplist
from page.page_sucess_order import PageSucess
from page.page_verify_order import PageVerifyOrder


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_login(self):
        return PageLogin(self.driver)

    @property
    def page_home(self):
        return PageHome(self.driver)

    @property
    def page_me(self):
        return PageMe(self.driver)

    @property
    def page_shoplist(self):
        return PageShoplist(self.driver)

    @property
    def page_shopdetail(self):
        return PageShopdetail(self.driver)

    @property
    def page_shopcart(self):
        return PageShopcart(self.driver)

    @property
    def page_sucess_order(self):
        return PageSucess(self.driver)

    @property
    def page_verify_order(self):
        return PageVerifyOrder(self.driver)

    @property
    def page_myorder(self):
        return PageMyorder(self.driver)