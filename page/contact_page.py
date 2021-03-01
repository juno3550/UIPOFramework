from conf.global_var import *
from util.ini_parser import IniParser
from util.find_element_util import *


# 通讯录页面元素定位及操作
class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        # 初始化指定ini配置文件及指定分组
        self.cf = IniParser(ELEMENT_FILE_PATH, "126mail_contactPersonPage")

    # 获取新建联系人按钮对象
    def get_contact_create_button_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.createButton").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 点击新建联系人按钮
    def click_contact_creat_button(self):
        self.get_contact_create_button_obj().click()

    # 获取姓名输入框对象
    def get_name_input_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.name").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 输入姓名操作
    def input_name(self, value):
        self.get_name_input_obj().send_keys(value)

    # 获取邮箱输入框对象
    def get_email_input_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.email").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 输入邮箱操作
    def input_email(self, value):
        self.get_email_input_obj().send_keys(value)

    # 获取星标联系人单选框对象
    def get_star_button_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.starContacts").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 点击星标联系人操作
    def click_star_button(self):
        self.get_star_button_obj().click()

    # 获取手机输入框对象
    def get_phone_input_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.phone").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 输入邮箱操作
    def input_phone(self, value):
        self.get_phone_input_obj().send_keys(value)

    # 获取备注输入框对象
    def get_remark_input_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.otherinfo").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 输入邮箱操作
    def input_remark(self, value):
        self.get_remark_input_obj().send_keys(value)

    # 获取确定按钮对象
    def get_confirm_button_obj(self):
        locate_method, locate_exp = self.cf.get_value("contactPersonPage.confirmButton").split(">")
        return find_element(self.driver, locate_method, locate_exp)

    # 点击星标联系人操作
    def click_confirm_button(self):
        self.get_confirm_button_obj().click()
