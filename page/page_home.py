from selenium.webdriver.common.by import By

from base.base import Base


class PageHome(Base):

    login_btn = By.CSS_SELECTOR, ".red"
    input_box = By.CSS_SELECTOR, "#q"
    search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
    goto_cart = By.CSS_SELECTOR, ".c-n"
    myorder = By.PARTIAL_LINK_TEXT, "我的订单"

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.base_click(self.login_btn)

    def input(self, x):
        self.base_input(self.input_box, x)

    def click_search(self):
        self.base_click(self.search_btn)

    def click_cart(self):
        self.base_click(self.goto_cart)

    def click_myorder(self):
        self.base_click(self.myorder)

    def get_image(self):
        self.base_get_image()

    


