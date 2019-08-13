from selenium import webdriver

class Testing:

    def __init__(self, driver):
        self.driver = driver



    def ClickOperation(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def SendInputOperation(self,xpath,input):
        self.driver.find_element_by_xpath(xpath).send_keys(input)



