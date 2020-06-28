# coding:utf-8
from src.browser import Browser
from src.utils.color import Color
from src.utils.calc import Calc


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
        print(time_prefix + Calc.current_time())

    def clock_in(self):
        selector = "attendance-card-time-stamp-clock-in"
        prefix = "CLOCK " + Color.get_colored(Color.BOLD, "IN") + " TIME: "
        self.clock_execute(selector, prefix)

        Color.print(Color.GREEN, "DAKOKU successful. Good luck!")

    def clock_out(self):
        selector = "attendance-card-time-stamp-clock-out"
        prefix = "CLOCK " + Color.get_colored(Color.BOLD, "OUT") + " TIME: "
        self.clock_execute(selector, prefix)

        Color.print(Color.GREEN, "DAKOKU successful. Good job today!")

    def exit(self):
        self.driver.close()
