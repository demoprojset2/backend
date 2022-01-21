from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import datetime 
driver = webdriver.Chrome()


driver.get("http://127.0.0.1:3000/")

'''
patientsbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[2]/button')
patientsbtn.click()
time.sleep(1)

'''

time.sleep(2)
doctorsbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button')
doctorsbtn.click()
time.sleep(1)

user = driver.find_element_by_id('name')
user.send_keys("Shrutii")
time.sleep(0.5)

firstname = driver.find_element_by_id('firstname')
time.sleep(1)
firstname.send_keys("shruti")
time.sleep(0.5)

lastname= driver.find_element_by_id('lastname')
lastname.send_keys("patil")
time.sleep(1)


speciality= driver.find_element_by_id('speciality')
speciality.send_keys("dentist")
time.sleep(1)

password = driver.find_element_by_id('password')
password.send_keys("qwryubftg")
time.sleep(1)


conpassword = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[6]/input')
conpassword.send_keys("qwryubftg")
time.sleep(1)

email = driver.find_element_by_id('email')
email.send_keys("gawandeshruti970@gmail.com")
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