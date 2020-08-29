from selenium.webdriver.common.by import By

from base.base import Base


class PageSucess(Base):

    submit_sucess = By.CSS_SELECTOR, ".erhuh>h3"
    goods_arrived_cost = By.CSS_SELECTOR, '[ value="pay_code=cod"]'
    confirm_cost = By.CSS_SELECTOR, ".button-confirm-payment"
    title = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"



    def get_text_cost(self):
        return self.base_get_text(self.submit_sucess)

    def click_goods_arrived(self):
        self.base_click(self.goods_arrived_cost)

    def click_confirm_cost(self):
        self.base_click(self.confirm_cost)

    def switch_me(self):
        self.base_switch_window(self.title)
