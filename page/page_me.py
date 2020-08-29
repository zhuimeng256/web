from selenium.webdriver.common.by import By

from base.base import Base


class PageMe(Base):

    myshop_btn = By.CSS_SELECTOR, ".index"
    quit_btn = By.PARTIAL_LINK_TEXT, "安全退出"
    home_btn = By.PARTIAL_LINK_TEXT, "首页"

    def isexist_myshop(self):
        return self.base_isexist(self.myshop_btn)

    def click_quit(self):
        self.base_click(self.quit_btn)

    def click_home(self):
        self.base_click(self.home_btn)
