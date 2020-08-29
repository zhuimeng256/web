from selenium.webdriver.common.by import By

from base.base import Base


class PageVerifyOrder(Base):

    submit_order = By.CSS_SELECTOR, ".gwc-qjs>span"
    receive = By.CSS_SELECTOR, ".consignee"


    def find(self):
        self.base_find(self.receive)

    def click_submit_order(self):
        self.base_click(self.submit_order)