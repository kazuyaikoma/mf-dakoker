# coding:utf-8
import datetime
from src.browser import Browser
from src.utils.colors import Colors


class AttendanceManager(object):

    def __init__(self):
        self.browser = Browser()
        self.driver = self.browser.driver

    def start(self):
        if self.login():
            self.clock_in()
            self.exit()

    def stop(self):
        if self.login():
            self.clock_out()
            self.exit()

    def login(self):
        return self.browser.login()

    def clock_execute(self, selector, time_prefix):
        if self.driver.current_url != self.browser.MYPAGE_URL:
            print("Please login.")

        self.driver.find_element_by_class_name(selector).click()
        print(time_prefix + self.current_time())

    def clock_in(self):
        selector = "attendance-card-time-stamp-clock-in"
        prefix = "CLOCK " + Colors.get_colored(Colors.BOLD, "IN") + " TIME: "
        self.clock_execute(selector, prefix)

        Colors.print(Colors.GREEN, "DAKOKU successful. Good luck!")

    def clock_out(self):
        selector = "attendance-card-time-stamp-clock-out"
        prefix = "CLOCK " + Colors.get_colored(Colors.BOLD, "OUT") + " TIME: "
        self.clock_execute(selector, prefix)

        Colors.print(Colors.GREEN, "DAKOKU successful. Good job today!")

    def current_time(self):
        return str(datetime.datetime.now()).split('.')[0]

    def exit(self):
        self.driver.close()
