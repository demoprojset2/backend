from pydoc import cli
from click import edit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import datetime 
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

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

signin = driver.find_element_by_link_text('Sign in').click()

name=driver.find_element_by_id("name")
name.send_keys("gawandeshruti970@gmail.com")

passw=driver.find_element_by_id("password")
passw.send_keys("qwryubftg")

driver.find_element_by_css_selector('#root > div > div > div.appForm > div > form > div:nth-child(3) > button').click()
time.sleep(1)
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
time.sleep(1)

#patientlist= driver.find_element_by_xpath('//*[@id="header"]/div/a[2]/button').click()
#time.sleep(1)



addAllergyDetail = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div[1]/button')
addAllergyDetail.click()
time.sleep(1)

substance = driver.find_element_by_xpath('//*[@id="validationCustom01"]')
substance.send_keys("alcohol")
time.sleep(1)

status = driver.find_element_by_xpath('//*[@id="validationCustom04"]/option[4]').click()
time.sleep(1)

critically = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div/form/div[1]/div/div[3]/select/option[4]').click()
time.sleep(1)

type = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div/form/div[1]/div/div[4]/select/option[3]').click()
time.sleep(1)

comments = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div/form/div[1]/div/div[5]/input')
comments.send_keys("stay Safe")
time.sleep(1)


save= driver.find_element_by_xpath('//*[@id="exampleModalCenter"]/div/div/form/div[2]/button[2]').click()
time.sleep(3)

#problemDetails

addProblem = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div[2]/button').click()
time.sleep(1)

problemname = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/input')
problemname.send_keys("Fever")
time.sleep(1)

severity = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/select/option[3]').click()
time.sleep(1)

status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div/div[3]/select/option[2]').click()
time.sleep(1)

startDate  = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div/div[4]/input')
startDate.send_keys('01/18/2022')
startDate.click()

saveChangws= driver.find_element_by_xpath('//*[@id="exampleModalCenter2"]/div/div/form/div[2]/button[2]').click()
time.sleep(3)

#AddPrescription
addPrescription = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div/button').click()
time.sleep(1)

medname = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div/div/form/div[1]/div/div[1]/input')
medname.send_keys("Paracetamol")
time.sleep(1)

manname = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div/div/form/div[1]/div/div[2]/input')
manname.send_keys("Farmson")
time.sleep(1)

doseamt = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div/div/form/div[1]/div/div[3]/input')
doseamt.send_keys("2")
time.sleep(1)

dosefrq = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div/div/form/div[1]/div/div[4]/select/option[2]')
dosefrq.click()
time.sleep(1)

dosedes = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div/div/form/div[1]/div/div[5]/input')
dosedes.send_keys("take medicine twice a day")
time.sleep(1)

driver.find_element_by_css_selector('#exampleModalCenter3 > div > div > form > div.modal-footer > button.btn.btn-success').click()
time.sleep(2)

#driver.find_element_by_link_text("Logout").click()
#time.sleep(1)
