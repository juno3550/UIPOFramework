from action.case_action import *
from util.excel_util import *
from conf.global_var import *
from util.datetime_util import *
from util.screenshot import take_screenshot


# 封装测试数据文件中用例的执行逻辑
# 测试数据文件中每个登录账号下，添加所有联系人数据
def batch_login_and_add_contact(test_data_file, browser_name, account_sheet_name):
        excel = Excel(test_data_file)
        # 获取登录账号sheet页数据
        excel.change_sheet(account_sheet_name)
        account_all_data = excel.get_all_row_data()
        account_headline_data = account_all_data[0]
        for account_row_data in account_all_data[1:]:
            # 执行登录用例
            account_row_data[ACCOUNT_TEST_TIME_COL] = get_english_datetime()
            if account_row_data[ACCOUNT_IS_EXECUTE_COL].lower() == "n":
                continue
            # 初始化浏览器
            driver = init_browser(browser_name)
            # 获取联系人数据sheet
            contact_data_sheet = account_row_data[ACCOUNT_DATA_SHEET_COL]
            try:
                # 默认以"退出"作为断言关键字
                login(driver, account_row_data[ACCOUNT_USERNAME_COL], account_row_data[ACCOUNT_PWD_COL], "退出")
                info("登录成功【用户名：{}, 密码：{}, 断言关键字：{}】".format(account_row_data[ACCOUNT_USERNAME_COL],
                                                            account_row_data[ACCOUNT_PWD_COL], "退出"))
                account_row_data[ACCOUNT_TEST_RESULT_COL] = "pass"
            except:
                error("登录失败【用户名：{}, 密码：{}, 断言关键字：{}】".format(account_row_data[ACCOUNT_USERNAME_COL],
                                                            account_row_data[ACCOUNT_PWD_COL], "退出"))
                account_row_data[ACCOUNT_TEST_RESULT_COL] = "fail"
                account_row_data[ACCOUNT_TEST_EXCEPTION_INFO_COL] = traceback.format_exc()
                account_row_data[ACCOUNT_SCREENSHOT_COL] = take_screenshot(driver)
            # 写入登录用例的测试结果
            excel.change_sheet("测试结果")
            excel.write_row_data(account_headline_data, "red")
            excel.write_row_data(account_row_data)
            excel.save()

            # 执行添加联系人用例
            excel.change_sheet(contact_data_sheet)
            contact_all_data = excel.get_all_row_data()
            contact_headline_data = contact_all_data[0]
            # 在测试结果中，一个账号下的联系人数据标题行仅写一次
            contact_headline_flag = True
            for contact_row_data in contact_all_data[1:]:
                if contact_row_data[CONTACT_IS_EXECUTE_COL].lower() == "n":
                    continue
                contact_row_data[CONTACT_TEST_TIME_COL] = get_english_datetime()
                try:
                    add_contact(driver, contact_row_data[CONTACT_NAME_COL], contact_row_data[CONTACT_EMAIL_COL],
                                contact_row_data[CONTACT_PHONE_COL], contact_row_data[CONTACT_IS_STAR_COL],
                                contact_row_data[CONTACT_REMARK_COL], contact_row_data[CONTACT_ASSERT_KEYWORD_COL])
                    info("添加联系人成功【姓名:{}, 邮箱:{}, 手机号:{}, 是否星标联系人:{}, "
                         "备注:{}, 断言关键字:{}】".format(contact_row_data[CONTACT_NAME_COL], contact_row_data[CONTACT_EMAIL_COL],
                                                   contact_row_data[CONTACT_PHONE_COL], contact_row_data[CONTACT_IS_STAR_COL],
                                                   contact_row_data[CONTACT_REMARK_COL], contact_row_data[CONTACT_ASSERT_KEYWORD_COL]))
                    contact_row_data[CONTACT_TEST_RESULT_COL] = "pass"
                except:
                    error("添加联系人失败【姓名:{}, 邮箱:{}, 手机号:{}, 是否星标联系人:{}, "
                         "备注:{}, 断言关键字:{}】".format(contact_row_data[CONTACT_NAME_COL], contact_row_data[CONTACT_EMAIL_COL],
                                                   contact_row_data[CONTACT_PHONE_COL], contact_row_data[CONTACT_IS_STAR_COL],
                                                   contact_row_data[CONTACT_REMARK_COL], contact_row_data[CONTACT_ASSERT_KEYWORD_COL]))
                    contact_row_data[CONTACT_TEST_RESULT_COL] = "fail"
                    contact_row_data[CONTACT_TEST_EXCEPTION_INFO_COL] = traceback.format_exc()
                    contact_row_data[CONTACT_SCREENSHOT_COL] = take_screenshot(driver)
                # 写入登录用例的测试结果
                excel.change_sheet("测试结果")
                if contact_headline_flag:
                    excel.write_row_data(contact_headline_data, "red")
                    contact_headline_flag = False
                excel.write_row_data(contact_row_data)
                excel.save()

            # 切换另一个账号时需先关闭浏览器，否则会自动登录
            driver.quit()


if __name__ == "__main__":
    batch_login_and_add_contact(TEST_DATA_FILE_PATH, "chrome", "126账号")
