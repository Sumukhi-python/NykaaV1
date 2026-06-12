import os.path
import pytest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    if browser == "edge":
        driver=webdriver.Edge()
        print("Launching Edge browser....")
    elif browser == "firefox":
        driver=webdriver.Firefox()
        print("Launching firefox browser....")
    else:
        driver=webdriver.Chrome()
        print("Launching Chrome browser....")
    return driver

def pytest_addoption(parser):  #this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #this will return the browser value to setup method
    return request.config.getoption("--browser")

###### pytest HTML Report ######
def pytest_configure(config):
    config._metadata['Project Name']='OrangeHRM'
    config._metadata['Module Name']='Login'
    config._metadata['Tester']='Sumukhi'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+".html"
