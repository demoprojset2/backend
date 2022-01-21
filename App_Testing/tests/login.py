#from lib2to3.pgen2 import driver
from selenium import webdriver
import time
import unittest
#import sys
#import os
#sys.path.append("/home/i1539/Desktop/final_project/onlineEHR/App_Testing") 
import sys
import os
#from turtle import home
sys.path.append("/home/i1550/Desktop/final_project/onlineEHR/") 
from App_Testing.Pages.patientlogin import plogin
from App_Testing.Pages.phomePage import HomePage
import HtmlTestRunner
driver = webdriver.Chrome()
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://127.0.0.1:3000/')

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/")
        login = plogin(driver)
        login.click_patient()
        login.enter_userid("45f69ba0-87ff-4676-a823-47eaa978b350")
        login.click_login()

        #paccount = HomePage(driver)
        #paccount.click_logout()

        #self.patientbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[2]/button').click()
        #self.time.sleep(1)
        #self.patientid = driver.find_element_by_xpath('//*[@id="patient_id"]')
        #self.patientid.send_keys('45f69ba0-87ff-4676-a823-47eaa978b350')
        #self.time.sleep(1)
        #self.signinbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/form/div[2]/button').click()
        #self.driver.find_element_by_link_text("Logout").click()
        #self.time.sleep(1)
        #@classmethod
        #def tearDownClass(cls):
        #  cls.driver.close()
        #  cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('output=/report'))
    




