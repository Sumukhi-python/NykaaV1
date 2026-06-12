from selenium.webdriver.common.by import By

class RecruitmentPage:
    #Locators
    lnk_recruitment_xpath="//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"
    lnk_vacancies_linktext="Vacancies"
    text_vcacancies_xpath="//h5[text()='Vacancies']"
    drpdwn_jobtitle_xpath="(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
    drpdwn_vacancy_xpath="(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
    drpdwn_hiringmanager_xpath="(//div[@class='oxd-select-text oxd-select-text--active'])[3]"
    drpdwn_status_xpath="(//div[@class='oxd-select-text oxd-select-text--active'])[4]"
    btn_search_xpath="//button[normalize-space()='Search']"
    text_recordsfound_xpath="//span[contains(normalize-space(),'Records Found')]"

    # Constructors
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def clickRecruitment(self):
        self.driver.find_element(By.XPATH, self.lnk_recruitment_xpath).click()

    def clickVacancies(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_vacancies_linktext).click()

    def getVacanciesFoundMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_vcacancies_xpath).is_displayed()
        except:
            False
    #
    # def selectJobTitle(self,jobtitle):
    #     s=self.driver.find_element(By.XPATH, self.drpdwn_jobtitle_xpath)
    #     s.select_by_visible_text(jobtitle)
    #
    # def selectVacancy(self,vacancy):
    #     s=self.driver.find_element(By.XPATH, self.drpdwn_vacancy_xpath)
    #     s.select_by_visible_text(vacancy)
    #
    # def selectHiringManager(self,hiringmanager):
    #     s=self.driver.find_element(By.XPATH, self.drpdwn_hiringmanager_xpath)
    #     s.select_by_visible_text(hiringmanager)
    #
    # def selectStatus(self,status):
    #     s=self.driver.find_element(By.XPATH, self.drpdwn_status_xpath)
    #     s.select_by_visible_text(status)
    #
    # def clickSearch(self):
    #     self.driver.find_element(By.XPATH, self.btn_search_xpath).click()
    #
    # def getRecordsFoundMsg(self):
    #     try:
    #         return self.driver.find_element(By.XPATH, self.text_recordsfound_xpath).is_displayed()
    #     except:
    #         False

