from xml.sax.xmlreader import Locator


from App_Testing.Locators.locators import Locators
class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.logout_link_linktest = Locators.logout_link_linktest

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktest).click()