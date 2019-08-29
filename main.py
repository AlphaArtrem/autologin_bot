import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    browser = webdriver.Chrome()
    with open("data.csv") as file:
        read = csv.reader(file, delimiter=":")

        count = 0;

        for row in read:
            if count < 3:
                browser.get("https://www.netflix.com/in/login")
                id = browser.find_element_by_id("id_userLoginId")
                id.send_keys(row[0])
                pwd = browser.find_element_by_id("id_password")
                pwd.send_keys(row[1])
                sign_in = browser.find_element_by_xpath("//button[@class='btn login-button btn-submit btn-small'][@type='submit']")
                sign_in.click()
            count += 1


if __name__ == '__main__':
    main()
