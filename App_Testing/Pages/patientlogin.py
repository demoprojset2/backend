from App_Testing.Locators.locators import Locators
class plogin():
    def __init__(self,driver):
        self.driver = driver
        self.patient_button_xpath = Locators.patient_button_xpath
        self.userid_textbox_xpath = Locators.userid_textbox_xpath
        self.signin_button_xpath = Locators.signin_button_xpath 

    def click_patient(self):
        self.driver.find_element_by_xpath(self.patient_button_xpath).click()
     
    def enter_userid(self,userid):
        self.driver.find_element_by_xpath(self.userid_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.userid_textbox_xpath).send_keys(userid)
    
    def click_login(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()
    
