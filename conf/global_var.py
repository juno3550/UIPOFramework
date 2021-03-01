import os


# 工程根路径
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 元素定位方法的ini配置文件路径
ELEMENT_FILE_PATH = os.path.join(PROJECT_ROOT_PATH, "conf", "elements_repository.ini")

# 驱动路径
CHROME_DRIVER = "E:\\auto_test_driver\\chromedriver.exe"
IE_DRIVER = "E:\\auto_test_driver\\IEDriverServer.exe"
FIREFOX_DRIVER = "E:\\auto_test_driver\\geckodriver.exe"

# 测试使用的浏览器
BROWSER_NAME = "chrome"

# 登录主页
LOGIN_URL = "https://mail.126.com"

# 日志配置文件路径
LOG_CONF_FILE_PATH = os.path.join(PROJECT_ROOT_PATH, "conf", "logger.conf")

# 测试用例文件路径
TEST_DATA_FILE_PATH = os.path.join(PROJECT_ROOT_PATH, "test_data", "测试用例.xlsx")

# 截图保存路径
SCREENSHOT_PATH = os.path.join(PROJECT_ROOT_PATH, "screenshot_path")

# 单元测试报告输出目录
UNITTEST_REPORT_PATH = os.path.join(PROJECT_ROOT_PATH, "report")

# 登录账号sheet页数据列号
ACCOUNT_USERNAME_COL = 1
ACCOUNT_PWD_COL = 2
ACCOUNT_DATA_SHEET_COL = 3
ACCOUNT_IS_EXECUTE_COL = 4
ACCOUNT_TEST_TIME_COL = 5
ACCOUNT_TEST_RESULT_COL = 6
ACCOUNT_TEST_EXCEPTION_INFO_COL = 7
ACCOUNT_SCREENSHOT_COL = 8

# 联系人sheet页数据列号
CONTACT_NAME_COL = 1
CONTACT_EMAIL_COL = 2
CONTACT_IS_STAR_COL = 3
CONTACT_PHONE_COL = 4
CONTACT_REMARK_COL = 5
CONTACT_ASSERT_KEYWORD_COL = 6
CONTACT_IS_EXECUTE_COL = 7
CONTACT_TEST_TIME_COL = 8
CONTACT_TEST_RESULT_COL = 9
CONTACT_TEST_EXCEPTION_INFO_COL = 10
CONTACT_SCREENSHOT_COL = 11


if __name__ == "__main__":
    print(PROJECT_ROOT_PATH)