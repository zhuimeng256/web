from selenium import webdriver


class GetDriver:
    driver = None

    URL = "http://www.myshop.com/"

    # 获取 driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取driver
            cls.driver = webdriver.Firefox()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(cls.URL)
        # 返回 driver
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空操作
            cls.driver = None