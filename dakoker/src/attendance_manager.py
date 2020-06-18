# coding:utf-8
import datetime
from src.account_manager import AccountManager


class AttendanceManager(object):

    def __init__(self):
        self.ac_manager = AccountManager()
        self.driver = self.ac_manager.driver

    def login(self):
        return self.ac_manager.login()

    def clock_in(self):
        if self.driver.current_url != self.ac_manager.MYPAGE_URL:
            print("Please login.")

        self.driver.find_element_by_class_name(
            "attendance-card-time-stamp-clock-in"
        ).click()
        print("CLOCK IN TIME: " + self.current_time())
        print("DAKOKU finished.")

    def clock_out(self):
        if self.driver.current_url != self.ac_manager.MYPAGE_URL:
            print("Please login.")

        self.driver.find_element_by_class_name(
            "attendance-card-time-stamp-clock-out"
        ).click()
        print("CLOCK OUT TIME: " + self.current_time())
        print("DAKOKU finished.")

    def current_time(self):
        return str(datetime.datetime.now()).split('.')[0]

    def exit(self):
        self.driver.close()
