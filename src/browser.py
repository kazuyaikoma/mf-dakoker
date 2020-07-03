# coding:utf-8
from pick import pick
from halo import Halo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from src.utils.color import Color
from src.user_info_manager import UserInfoManager


class Browser(object):
    TIMEOUT = 3
    ROOT_URL = "https://attendance.moneyforward.com"
    LOGIN_URL = ROOT_URL + "/employee_session/new"
    MYPAGE_URL = ROOT_URL + "/my_page"
    ATTENDANCE_URL = MYPAGE_URL + "/attendances"
    LOGIN_SUCCEED = "Login Success."
    LOGIN_FAILED = "Login Failed."

    DRIVER = 'DRIVER'
    SAFARI = 'Safari Drievr'
    CHROME = 'Chrome Drievr'

    def __init__(self):
        self.info_manager = UserInfoManager()
        self.user_info = self.info_manager.get()
        self.set_driver_to_userinfo()
        self.set_driver()

    def set_driver(self):
        if self.user_info[self.DRIVER] == self.SAFARI:
            # TODO: make driver headless
            self.driver = webdriver.Safari()
        else:
            options = webdriver.ChromeOptions()
            options.headless = True
            self.driver = webdriver.Chrome(chrome_options=options)

    def set_driver_to_userinfo(self):
        if self.DRIVER not in self.user_info.keys():
            message = 'Please select your browser driver:'
            options = [self.SAFARI, self.CHROME]
            option, _ = pick(options, message)
            self.user_info[self.DRIVER] = option

    def login(self):
        spinner = Halo(text='Loading login page...', spinner='dots')
        spinner.start()
        self.driver.get(self.LOGIN_URL)
        spinner.succeed("Login page loaded.")

        spinner = Halo(text='Login...', spinner='dots')
        spinner.start()
        return self.login_with_user_info(spinner)

    def login_with_user_info(self, spinner):
        self.driver.find_element_by_id(
            "employee_session_form_office_account_name"
        ).send_keys(self.user_info[self.info_manager.CORP_ID])
        self.driver.find_element_by_id(
            "employee_session_form_account_name_or_email"
        ).send_keys(self.user_info[self.info_manager.USER_ID])
        self.driver.find_element_by_id(
            "employee_session_form_password"
        ).send_keys(self.user_info[self.info_manager.USER_PASS])

        self.driver.find_element_by_class_name(
            "attendance-before-login-card-button"
        ).click()

        return self.check_login(spinner)

    def check_login(self, spinner):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "attendance-card-title")
                )
            )
            self.info_manager.save(self.user_info)
            spinner.succeed(self.LOGIN_SUCCEED)
            return True

        except TimeoutException:
            if self.driver.find_elements(By.CLASS_NAME, "is-error") != 0:
                Color.print(
                    Color.RED,
                    "\nCompany ID, User ID or Password is wrong."
                )
                UserInfoManager.remove()
                spinner.fail(self.LOGIN_FAILED)
                return self.login()
            else:
                Color.print(Color.RED, "\nLogin Timeout.")
                spinner.fail(self.LOGIN_FAILED)
                return False

    def open_attendance(self):
        if self.login():
            spinner = Halo(text='Loading attendance page...', spinner='dots')
            self.driver.get(self.ATTENDANCE_URL)

        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "modal-controller-my-page-attendances")
                )
            )
            spinner.succeed('Attendance page loaded.')
            return True

        except TimeoutException:
            return False
