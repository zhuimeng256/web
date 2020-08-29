from selenium.webdriver.common.by import By

from base.base import Base


class PageMyorder(Base):

    wait_cost = By.CSS_SELECTOR, ".selected"
    instance_cost =By.CSS_SELECTOR, ".ps_lj"
    title ="我的订单"



    def click_wait_cost(self):
        self.base_click(self.wait_cost)

    def click_instance_cost(self):
        self.base_click(self.instance_cost)

    def switch_me(self):
        self.base_switch_window(self.title)