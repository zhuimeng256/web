from selenium.webdriver.common.by import By

from base.base import Base


class PageShopcart(Base):

    goto_settment = By.CSS_SELECTOR, ".gwc-qjs"
    full_select = By.CSS_SELECTOR, ".checkCartAll"

    def isexist_settment(self):
        return self.base_isexist(self.goto_settment)

    def click_select(self):
        element = self.base_find(self.full_select)
        if not element.is_selected():
            element.click()

    def click_settment(self):
        self.base_click(self.goto_settment)

