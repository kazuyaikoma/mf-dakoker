# coding:utf-8
from src.account_manager import AccountManager


def main():
    company_id = ""
    user_id = ""
    user_pass = ""

    user_info = {}
    user_info['company_id'] = company_id
    user_info['id'] = user_id
    user_info['pass'] = user_pass

    manager = AccountManager(user_info)
    manager.login()


if __name__ == "__main__":
    main()
