from conf.global_var import *
from util.ini_parser import IniParser
from util.find_element_util import *


# 登录后主页元素定位及操作
class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # 初始化指定ini配置文件及指定分组
        self.cf = IniParser(ELEMENT_FILE_PATH, "126mail_homePage")

    # 获取“通讯录”按钮对象
    def get_contact_button_obj(self):
        locate_method, locate_exp = self.cf.get_value("homePage.addressLink").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 点击“通讯录”按钮
    def click_contact_button(self):
        self.get_contact_button_obj().click()

