from selenium import webdriver
import time
import unittest
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:3000/")
patientbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[2]/button').click()
time.sleep(1)
patientid = driver.find_element_by_xpath('//*[@id="patient_id"]')
patientid.send_keys('45f69ba0-87ff-4676-a823-47eaa978b350')
time.sleep(1)
signinbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/form/div[2]/button').click()
driver.find_element_by_link_text("Logout").click()
time.sleep(1)