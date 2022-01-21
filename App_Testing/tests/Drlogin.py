import sys
from turtle import home
sys.path.append("/home/i1539/Desktop/component/onlineEHR-main/") 

from selenium import webdriver
import time
import unittest
#from App_Testing.Pages.register import register
from App_Testing.Pages.loginpage import loginpage
from App_Testing.Pages.homepage import homepage


class LOginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.get('http://127.0.0.1:3000/sign-up/')

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/sign-in")
        login=loginpage(driver)
        login.enter_username("")
        login.enter_pass("")
        login.click_login()
        driver.forward()
        driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="validationCustom01"]').send_keys("mrudula")
        self.driver.find_element_by_xpath('//*[@id="validationCustom05"]').send_keys("6624439162")
        self.driver.find_element_by_xpath('//*[@id="validationCustom04"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="validationCustomUsername"]').send_keys("gawandeaish2011@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="validationCustom03"]').send_keys("Shegaon Dist : Buldhana")