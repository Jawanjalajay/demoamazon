from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class loginpage():
    click_signin_dashbopard_xpath=(By.XPATH,"//div[@class='nav-line-1-container']")
    text_email_or_phone_xpath=(By.XPATH,"//input[@id='ap_email']")
    click_continue_btn_xpath=(By.XPATH,"//input[@id='continue']")
    text_password_xpath=(By.XPATH,"//input[@id='ap_password']")
    click_login_btn_xpath=(By.XPATH,"//input[@id='signInSubmit']")
    click_menu_btn_xpath=(By.XPATH,"//i[@class='hm-icon nav-sprite']")
    click_logout_btn_xpath=(By.XPATH,"//a[@class='hmenu-item'][normalize-space()='Sign Out']")

    def __init__(self,driver):
        self.driver=driver

    def click_signin_dashboard(self):
        self.driver.find_element(*loginpage.click_signin_dashbopard_xpath).click()

    def enter_email_or_phone(self,email_or_phone):
        self.driver.find_element(*loginpage.text_email_or_phone_xpath).send_keys(email_or_phone)

    def click_continue_btn(self):
        self.driver.find_element(*loginpage.click_continue_btn_xpath).click()

    def enter_password(self,password):
        self.driver.find_element(*loginpage.text_password_xpath).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*loginpage.click_login_btn_xpath).click()

    def click_menu_btn(self):
        self.driver.find_element(*loginpage.click_menu_btn_xpath).click()

    def click_logout_btn(self):
        self.driver.find_element(*loginpage.click_logout_btn_xpath).click()

    def login_status(self):
        try:
            self.driver.find_element(*loginpage.click_menu_btn_xpath)
            return True
        except NoSuchElementException:
            return False
