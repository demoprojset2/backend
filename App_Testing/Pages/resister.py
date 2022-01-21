from App_Testing.Locators.locators import Locators
class register():
    def __init__(self,driver):
        self.driver = driver

    def register(self):
        self.driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button').click()
        self.driver.find_element_by_id('username').send_keys("")
        self.driver.find_element_by_id('firstname').send_keys("6624439162")
        self.driver.find_element_by_id('lastname')
        self.driver.find_element_by_id('speciality').send_keys("6624439162")
        self.driver.find_element_by_id('password').send_keys("")
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[6]/input').send_keys("")
        self.driver.find_element_by_id('email').send_keys("me@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="validationCustom04"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/form/div[9]/button').click()

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Firefox()


driver.get("http://127.0.0.1:3000/")

patientsbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[2]/button')
patientsbtn.click()
time.sleep(1)
time.sleep(2)
doctorsbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button')
doctorsbtn.click()
time.sleep(1)

user = driver.find_element_by_id('name')
user.send_keys("aishwaryaa")
time.sleep(0.5)

firstname = driver.find_element_by_id('firstname')
time.sleep(1)
firstname.send_keys("aishwarya")
time.sleep(0.5)

lastname= driver.find_element_by_id('lastname')
lastname.send_keys("patil")
time.sleep(1)


speciality= driver.find_element_by_id('speciality')
speciality.send_keys("Dermatologists")
time.sleep(1)

password = driver.find_element_by_id('password')
password.send_keys("Aishwarya")
time.sleep(1)


conpassword = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[6]/input')
conpassword.send_keys("Aishwarya")
time.sleep(1)

email = driver.find_element_by_id('email')
email.send_keys("aishpatil19999@gmail.com")
time.sleep(1)


time.sleep(1)
gender = driver.find_element_by_xpath('//*[@id="validationCustom04"]/option[3]').click()

time.sleep(2)
submitbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/form/div[9]/button')
# /html/body/div/div/div/div[3]/div/form/div[9]/button
submitbtn.click()
driver.get('http://127.0.0.1:3000/sign-in/')

driver.forward()
time.sleep(2)

name=driver.find_element_by_id("name")
name.send_keys("aishpatil19999@gmail.com")

passw=driver.find_element_by_id("password")
passw.send_keys("Aishwarya")

driver.find_element_by_css_selector('#root > div > div > div.appForm > div > form > div:nth-child(3) > button').click()
driver.get('http://127.0.0.1:3000/docdash')
driver.forward()
'''
