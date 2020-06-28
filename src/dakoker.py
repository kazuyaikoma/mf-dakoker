# coding:utf-8
import fire

from src.user_info_manager import UserInfoManager
from src.attendance_manager import AttendanceManager


class Dakoker(object):

    def start(self):
        AttendanceManager().start()

    def stop(self):
        AttendanceManager().stop()

    def clear(self):
        UserInfoManager.remove_with_message()


def main():
    fire.Fire(Dakoker)
