from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import datetime 
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

driver.get("http://127.0.0.1:3000/")
time.sleep(2)
doctorsbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button')
doctorsbtn.click()
time.sleep(1)

signin = driver.find_element_by_link_text('Sign in').click()

name=driver.find_element_by_id("name")
name.send_keys("gawandeshruti970@gmail.com")

passw=driver.find_element_by_id("password")
passw.send_keys("qwryubftg")
driver.find_element_by_css_selector('#root > div > div > div.appForm > div > form > div:nth-child(3) > button').click()
time.sleep(3)

#patientlist
patientlist= driver.find_element_by_xpath('//*[@id="header"]/div/a[2]/button').click()
time.sleep(1)

searchbar = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/section/div/form/input')
searchbar.send_keys("mrudula")
time.sleep(1)

subbtn = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/section/div/form/button').click()
time.sleep(1)

adddetail = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/section/div/div/div/div[2]/div[1]/i')
adddetail.click()
time.sleep(3)

viewpatient = driver.find_element_by_css_selector('/html/body/div/div/div/div[2]/div/section/div/div/div/div[2]/div[3]/i').click()
time.sleep(2)
#remaining