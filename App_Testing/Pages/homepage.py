class homepage():
    def __init__(self,driver):
        self.driver = driver
    def enter_values(self):
        self.driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="validationCustom01"]').send_keys("mrudula")
        self.driver.find_element_by_xpath('//*[@id="validationCustom05"]').send_keys("6624439162")
        self.driver.find_element_by_xpath('//*[@id="validationCustom04"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="validationCustomUsername"]').send_keys("gawandeaish2011@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="validationCustom03"]').send_keys("Shegaon Dist : Buldhana")