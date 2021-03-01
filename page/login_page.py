from conf.global_var import *
from util.ini_parser import IniParser
from util.find_element_util import *


# 登录页面元素定位及操作
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # 初始化跳转登录页面
        self.driver.get(LOGIN_URL)
        # 初始化指定ini配置文件及指定分组
        self.cf = IniParser(ELEMENT_FILE_PATH, "126mail_loginPage")

    # 获取frame元素对象
    def get_frame_obj(self):
        locate_method, locate_exp = self.cf.get_value("loginPage.frame").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 切换frame
    def switch_frame(self):
        self.driver.switch_to.frame(self.get_frame_obj())

    # 获取用户名输入框元素对象
    def get_username_input_obj(self):
        locate_method, locate_exp = self.cf.get_value("loginPage.username").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 清空用户名输入框操作
    def clear_username(self):
        self.get_username_input_obj().clear()

    # 输入用户名操作
    def input_username(self, value):
        self.get_username_input_obj().send_keys(value)

    # 获取密码输入框元素对象
    def get_pwd_input_obj(self):
        locate_method, locate_exp = self.cf.get_value("loginPage.password").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 输入密码操作
    def input_pwd(self, value):
        self.get_pwd_input_obj().send_keys(value)

    # 获取登录按钮对象
    def get_login_buttion_obj(self):
        locate_method, locate_exp = self.cf.get_value("loginPage.loginbutton").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 点击登录按钮操作
    def click_login_button(self):
        self.get_login_buttion_obj().click()
