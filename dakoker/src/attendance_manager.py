# coding:utf-8
import datetime
from src.account_manager import AccountManager
from src.utils.colors import Colors


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
        print("CLOCK " + Colors.get_colored(Colors.BOLD, "IN") + " TIME: "
              + self.current_time())
        Colors.print(Colors.GREEN, "DAKOKU successful. Good luck!")

    def clock_out(self):
        if self.driver.current_url != self.ac_manager.MYPAGE_URL:
            print("Please login.")

        self.driver.find_element_by_class_name(
            "attendance-card-time-stamp-clock-out"
        ).click()
        print("CLOCK " + Colors.get_colored(Colors.BOLD, "OUT") + " TIME: "
              + self.current_time())
        Colors.print(Colors.GREEN, "DAKOKU successful. Good job today!")

    def current_time(self):
        return str(datetime.datetime.now()).split('.')[0]

    def exit(self):
        self.driver.close()
