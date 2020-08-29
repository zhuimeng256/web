from selenium.webdriver.common.by import By

from base.base import Base


class PageShoplist(Base):

    shoplist_simply = By.PARTIAL_LINK_TEXT, "小米手机5,十余项黑科技，很轻狠快"


    def click_shoplist(self):
        self.base_click(self.shoplist_simply)

    
