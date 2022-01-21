class loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.username="name"
        self.password="password"
        self.loginbtn="#root > div > div > div.appForm > div > form > div:nth-child(3) > button"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username).send_keys(username)    

    def enter_pass(self,password):
        self.driver.find_element_by_id(self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_css_selector(self.loginbtn).click()    