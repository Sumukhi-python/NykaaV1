from selenium.webdriver.common.by import By

class HomePage:
    #Locators
    txt_username_xpath="//input[@name='username']"
    txt_password_xpath="//input[@name='password']"
    btn_login_xpath="//button[normalize-space()='Login']"
    text_confmsg_xpath="//h6[normalize-space()='Dashboard']"
    img_profile_class="oxd-userdropdown-img"
    lnk_logout_linktext="Logout"

    #Constructors
    def __init__(self, driver):
        self.driver = driver

    #Action methods
    def setUsername(self,username):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_confmsg_xpath).is_displayed()
        except:
            None

    def clickProfile(self):
        self.driver.find_element(By.CLASS_NAME,self.img_profile_class).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_logout_linktext).click()
