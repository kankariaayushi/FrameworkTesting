from selenium import webdriver
from src import LocalConstant
from src.ClassTesting import Testing
import json
from pprint import pprint


def JsonLoad(filename1):
    with open(filename1,encoding='utf-8') as fobj:
        data1= json.load(fobj)

        #print(type(json_load))
        #pprint(data)
    pprint(data1)

def JsonDump():
    pass



if __name__ == '__main__':
    # drive_path="D:\Python_tutorials\chromedriver.exe"
    # browser=webdriver.Chrome(executable_path=drive_path)
    # browser.get("https://www.google.com/")
    # browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[2]').click()

    # drive_path = "D:\Python_tutorials\chromedriver.exe"
    # browser_obj=webdriver.Chrome(executable_path=drive_path)
    # #input_text=""
    # browser_obj.get("https://www.google.com/")
    # Testing_obj= Testing(browser_obj)
    # Testing_obj.SendInputOperation(LocalConstant.GOOGLE_SEARCH_TEXTBOX,"python")
    # Testing_obj.ClickOperation(LocalConstant.SEARCH_BOX)

    JsonLoad("LocalConstant.json")




