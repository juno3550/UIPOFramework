from business_process.batch_login import *
from business_process.batch_login_and_add_contact import *
from conf.global_var import *


# 示例组装：冒烟测试
def smoke_test():
    batch_login(TEST_DATA_FILE_PATH, "chrome", "126账号")


# 示例组装：全量测试
def full_test():
    batch_login_and_add_contact(TEST_DATA_FILE_PATH, "chrome", "126账号")


