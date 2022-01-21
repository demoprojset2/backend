from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import datetime 

driver = webdriver.Chrome()

#driver.set_window_size(1366,768)
driver.get('http://127.0.0.1:3000/sign-in/')

driver.forward()
time.sleep(2)

name=driver.find_element_by_id("name")
name.send_keys("gawandeshruti970@gmail.com")

passw=driver.find_element_by_id("password")
passw.send_keys("qwryubftg")

driver.find_element_by_css_selector('#root > div > div > div.appForm > div > form > div:nth-child(3) > button').click()
time.sleep(1)

driver.get('http://127.0.0.1:3000/docdash')
driver.forward()
time.sleep(3)

addpatientbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button').click()
time.sleep(1)

name = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[1]/input')
name.send_keys("renuka")
time.sleep(1)

phoneNumber = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[2]/input')
phoneNumber.send_keys("9503506363")
time.sleep(1)


gender = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[3]/select/option[3]').click()
time.sleep(1)

email = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[4]/div/input') 
email.send_keys("renukagawande58@gmail.com")
time.sleep(1)


address = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[5]/input')
address.send_keys("Shegaon ,Dist : Buldhana")
time.sleep(1)

dob = driver.find_element_by_name('dob')
dob.send_keys("08/20/1996")
dob.click()
time.sleep(1)

weight = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[7]/input')
weight.send_keys("40")
time.sleep(1)

height = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[8]/input')
height.send_keys("152")
time.sleep(1)
'''
dateAdded = driver.find_element_by_xpath('//*[@id="validationCustom01"]')
now = datetime.datetime.now()
tday = now.strftime("%m-%d-%Y")
dateAdded.send_keys(tday)
time.sleep(1)
'''
dateAdded = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[9]/input')
dateAdded.send_keys("01/24/2022")
dateAdded.click()
time.sleep(2)

BPs = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[10]/input')
BPs.send_keys("120")
time.sleep(1)

BPa = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[11]/input')
BPa.send_keys("80")
time.sleep(1)


temperatue = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[12]/input')
temperatue.send_keys("96")
time.sleep(1)

pulse = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[13]/input')
pulse.send_keys("100")
time.sleep(1)

smokingstatus = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[14]/select/option[2]').click()
time.sleep(1)

drinkingstatus = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[15]/select/option[2]').click()
time.sleep(1)


addpatientbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/form/div[2]/button')
addpatientbtn.click()
#time.sleep(1)
driver.get("http://127.0.0.1:3000/viewdetails")
 
# one step forward in browser history
driver.forward()