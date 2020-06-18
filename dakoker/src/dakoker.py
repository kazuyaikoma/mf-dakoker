# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    company_id = ""
    user_id = ""
    user_pass = ""

    print(user_id + " で打刻します...")

    driver = webdriver.Chrome()

    driver.get("https://attendance.moneyforward.com/employee_session/new")

    driver.find_element_by_id(
        "employee_session_form_office_account_name"
    ).send_keys(company_id)
    driver.find_element_by_id(
        "employee_session_form_account_name_or_email"
    ).send_keys(user_id)
    driver.find_element_by_id(
        "employee_session_form_password"
    ).send_keys(user_pass)

    driver.find_element_by_class_name(
        "attendance-before-login-card-button"
    ).click()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "attendance-card-title")
            )
        )
    except TimeoutException:
        print('ログイン中にタイムアウトしました。')

    # 出勤
    # driver.find_element_by_class_name(
    #     "attendance-card-time-stamp-clock-in"
    # ).click()
    # 退勤
    driver.find_element_by_class_name(
        "attendance-card-time-stamp-clock-out"
    ).click()

    print("打刻が完了しました。")

    driver.close()


if __name__ == "__main__":
    main()
