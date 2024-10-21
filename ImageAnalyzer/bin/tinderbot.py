from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from login import username, password
from analyze import image_analysis

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/chromedriver.exe')

    def login(self):
        self.driver.get('https://tinder.com/')


        sleep(7)

        signin = self.driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        signin.click()

        sleep(5)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[0])
        moreop = self.driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/button')
        moreop.click()
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[0])
        facebook = self.driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        facebook.click()
        facebook.send_keys(Keys.ENTER)
        accept = self.driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[2]/div/div/div[1]/button')
        accept.click()

        sleep(5)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        login_btn.click()


