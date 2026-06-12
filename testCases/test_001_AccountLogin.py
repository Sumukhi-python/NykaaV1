import time
import os

import pytest

from pageobjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # for Logging

class Test_001_AccountLogin:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_account_login(self,setup):
        self.logger.info("*** test_001_AccountLogin started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Launching Application ***")
        self.driver.maximize_window()
        time.sleep(5)
        self.hp=HomePage(self.driver)
        self.hp.setUsername(ReadConfig.getUsername())
        self.hp.setPassword(ReadConfig.getPassword())
        self.hp.clickLogin()
        time.sleep(5)
        self.logger.info("*** Logged into the Application ***")
        self.msg=self.hp.getconfirmationmsg()
        if self.msg:
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_login.png")
            self.driver.quit()
            assert False
        self.logger.info("*** test_001_AccountLogin finished ***")

