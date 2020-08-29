from selenium.webdriver.common.by import By

from base.base import Base


class PageShopdetail(Base):

    joincart = By.CSS_SELECTOR, "#join_cart"
    sucess_join = By.CSS_SELECTOR, ".conect-title>span"
    iframe_name = "layui-layer-iframe1"
    close_frame = By.CSS_SELECTOR, ".layui-layer-ico"
    goto_cart = By.CSS_SELECTOR, ".c-n"
    cart_frame_id = By.CSS_SELECTOR, "#layui-layer-iframe1"
    goto_home = By.PARTIAL_LINK_TEXT, "首页"


    def click_joincard(self):
        self.base_click(self.joincart)

    def sucess_join_text(self):
        return self.base_get_text(self.sucess_join)

    def switch_frame(self):
        # self.base_switch_frame(self.iframe_name)
        self.base_switch_frame(self.base_find(self.cart_frame_id))

    def switch_default(self):
        self.base_default_content()

    def click_close(self):
        self.base_click(self.close_frame)

    def click_gocart(self):
        self.base_click(self.goto_cart)

    def click_gohome(self):
        self.base_click(self.goto_home)
