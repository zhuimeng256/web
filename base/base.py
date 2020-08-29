import time
from selenium.webdriver.support.wait import WebDriverWait

from base.get_logger import GetLogger

log = GetLogger().get_logger()

class Base:
    def __init__(self, driver):
        log.info("[base]: 正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    def base_find(self, loc, timeout = 20, poll = 0.5):
        log.info("[base]: 正在定位:{} 元素，默认定位超时时间为: {}".format(loc, timeout))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def base_click(self, loc):
        log.info("[base]: 正在对:{} 元素实行点击事件".format(loc))
        self.base_find(loc).click()

    def base_input(self, loc, x):
        element = self.base_find(loc)
        log.info("[base]: 正在对:{} 元素实行清空".format(loc))
        element.clear()
        element.send_keys(x)

    def base_isexist(self, loc):
        try:
            self.base_find(loc, 7, 1)
            log.info("[base]: {} 元素查找成功，存在页面".format(loc))
            return True
        except:
            log.info("[base]: {} 元素查找失败，不存在当前页面".format(loc))
            return False

    def base_get_text(self, loc):
        log.info("[base]: 正在获取:{} 元素文本值".format(loc))
        return self.base_find(loc).text

    def base_get_image(self):
        log.info("[base]: 断言出错，调用截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))


    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)


    def base_default_content(self):
        self.driver.switch_to.default_content()

    def base_switch_window(self, title):
        log.info("正在执行切换title值为：{}窗口 ".format(title))
        self.driver.switch_to.window(self.base_get_title_handle(title))

    def base_get_title_handle(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                return handle
