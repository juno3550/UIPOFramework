from selenium import webdriver
import traceback
import time
from page.contact_page import ContactPage
from page.home_page import HomePage
from page.login_page import LoginPage
from conf.global_var import *
from util.log_util import *


# 初始化浏览器
def init_browser(browser_name):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(CHROME_DRIVER)
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(FIREFOX_DRIVER)
    elif browser_name.lower() == "ie":
        driver = webdriver.Ie(IE_DRIVER)
    else:
        return "Error browser name!"
    return driver


def assert_word(driver, text):
    assert text in driver.page_source


# 登录流程封装
def login(driver, username, pwd, assert_text):
    login_page = LoginPage(driver)
    login_page.switch_frame()
    login_page.clear_username()
    login_page.input_username(username)
    login_page.input_pwd(pwd)
    login_page.click_login_button()
    time.sleep(1)
    assert_word(driver, assert_text)


# 添加联系人流程封装
def add_contact(driver, name, email, phone, is_star, remark, assert_text):
    home_page = HomePage(driver)
    home_page.click_contact_button()
    contact_page = ContactPage(driver)
    contact_page.click_contact_creat_button()
    contact_page.input_name(name)
    contact_page.input_email(email)
    contact_page.input_phone(phone)
    contact_page.input_remark(remark)
    if is_star == "是":
        contact_page.click_star_button()
    contact_page.click_confirm_button()
    time.sleep(2)
    assert_word(driver, assert_text)


def quit(driver):
    driver.quit()


if __name__ == "__main__":
    driver = init_browser("chrome")
    login(driver, "juno3550", "258978aa", "退出")
    add_contact(driver, "铁蛋", "asfhi@123.com", "12222222222", "是", "这是备注", "铁蛋")
    # quit(driver)



