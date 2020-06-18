# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from IPython import embed


class AccountManager(object):
    TIMEOUT = 5
    LOGIN_URL = "https://attendance.moneyforward.com/employee_session/new"
    MYPAGE_URL = "https://attendance.moneyforward.com/my_page"

    def __init__(self, user_info):
        self.company_id = user_info['company_id']
        self.user_id = user_info['id']
        self.user_pass = user_info['pass']
        self.driver = webdriver.Chrome()

    def login(self):
        print(self.user_id + " でログインします...")
        self.driver.get(self.LOGIN_URL)
        self.driver.find_element_by_id(
            "employee_session_form_office_account_name"
        ).send_keys(self.company_id)
        self.driver.find_element_by_id(
            "employee_session_form_account_name_or_email"
        ).send_keys(self.user_id)
        self.driver.find_element_by_id(
            "employee_session_form_password"
        ).send_keys(self.user_pass)

        self.driver.find_element_by_class_name(
            "attendance-before-login-card-button"
        ).click()

        return self.check_login_error()

    def check_login_error(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "attendance-card-title")
                )
            )
            print("ログインしました。")
            embed()

            return True
        except TimeoutException:
            print("ログイン中にタイムアウトしました。")

            return False

    def clock_in(self):
        if self.driver.current_url != self.MYPAGE_URL:
            return False

        self.driver.find_element_by_class_name(
            "attendance-card-time-stamp-clock-in"
        ).click()
        print("出勤開始: ")

        return True

    def clock_out(self):
        if self.driver.current_url != self.MYPAGE_URL:
            return False

        self.driver.find_element_by_class_name(
            "attendance-card-time-stamp-clock-out"
        ).click()
        print("打刻が完了しました。")

        return True

    def exit(self):
        self.driver.close()
