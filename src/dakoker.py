# coding:utf-8
import sys
import fire

from src.user_info_manager import UserInfoManager
from src.stamp_manager import StampManager


class Dakoker(object):

    def start(self):
        StampManager().stamp(sys._getframe().f_code.co_name)

    def end(self):
        StampManager().stamp(sys._getframe().f_code.co_name)

    def start_break(self):
        StampManager().stamp(sys._getframe().f_code.co_name)

    def end_break(self):
        StampManager().stamp(sys._getframe().f_code.co_name)

    def clear(self):
        UserInfoManager.remove_with_message()


def main():
    fire.Fire(Dakoker)
