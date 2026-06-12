import time
import os
from pageobjects.HomePage import HomePage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # for Logging

class Test_001_AccountLogin2:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    path=os.path.abspath(os.curdir)+"\\testData\\OrangeHRM_LoginData.xlsx"

    def test_account_login(self,setup):
        self.logger.info("*** test_001_AccountLogin2 started DataDriven***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Launching Application ***")
        self.driver.maximize_window()
        time.sleep(10)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]
        for r in range(2,self.rows+1):
            self.hp = HomePage(self.driver)
            self.username=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            self.hp.setUsername(self.username)
            self.hp.setPassword(self.password)
            self.hp.clickLogin()
            time.sleep(5)
            self.target=self.hp.getconfirmationmsg()
            if self.exp=='Valid':
                if self.target==True:
                    lst_status.append('Pass')
                else:
                    lst_status.append('Fail')
                self.hp.clickProfile()
                time.sleep(2)
                self.hp.clickLogout()
                time.sleep(3)
            else:
                lst_status.append('Pass')
        self.driver.quit()
        #final Validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("*** test_001_AccountLogin2 finished Data Driven ***")

