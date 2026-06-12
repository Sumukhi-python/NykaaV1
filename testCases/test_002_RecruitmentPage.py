from ctypes import GetLastError

import pytest
import time
import os
from pageobjects.HomePage import HomePage
from pageobjects.RecruimentPage import RecruitmentPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # for Logging

class Test_Recruitment:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    user=ReadConfig.getUsername()
    passwd=ReadConfig.getPassword()

    @pytest.mark.regression
    def test_recruitment_page(self,setup):
        self.logger.info("***** Recruitment Page *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(10)
        self.hp=HomePage(self.driver)
        self.hp.setUsername(self.user)
        self.hp.setPassword(self.passwd)
        self.hp.clickLogin()
        time.sleep(3)
        self.rp=RecruitmentPage(self.driver)
        self.rp.clickRecruitment()
        time.sleep(2)
        self.rp.clickVacancies()
        time.sleep(2)
        self.msg=self.rp.getVacanciesFoundMsg()
        if self.msg==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_recruitment_page.png")
            assert False
        # self.rp.selectJobTitle("Account Assistant")
        # time.sleep(2)
        # self.rp.selectVacancy("test")
        # time.sleep(2)
        # self.rp.selectHiringManager("Rahul Patil")
        # time.sleep(2)
        # self.rp.selectStatus("Active")
        # time.sleep(2)
        # self.rp.clickSearch()
        # time.sleep(6)
        # self.msg=self.rp.getRecordsFoundMsg()
        # if self.msg==True:
        #     assert True
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_recruitment_page.png")
        #     assert False
        self.driver.quit()
        self.logger.info("*** test_002_Recruitment finished ***")


