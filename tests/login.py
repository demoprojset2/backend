from selenium import webdriver
from selenium.webdriver.support.select import Select
from django.test import LiveServerTestCase

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:3000/sign-in/')

name=driver.find_element_by_id("name")
name.send_keys("gawandeshruti970@gmail.com")
passw=driver.find_element_by_id("password")
passw.send_keys("qwryubftg")

driver.find_element_by_css_selector('#root > div > div > div.appForm > div > form > div:nth-child(3) > button').click()

driver.forward()