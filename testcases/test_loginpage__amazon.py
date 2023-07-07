import time

from pageObject.loginPage import loginpage
from utilities.readproperties import readconfig
from utilities.logger import LogJenerator

class Test_login():
    url=readconfig.geturl()
    email_or_phone=readconfig.getemail_or_phone()
    password=readconfig.getpassword()
    log=LogJenerator.loggen()

    def test_login_001(self,setup):
        self.driver=setup
        self.log.info('test_login__001 started')
        self.log.info('opening browser')
        self.driver.get(self.url)
        self.log.info('go to this url--> '+self.url)
        self.lp=loginpage(self.driver)
        self.lp.click_signin_dashboard()
        time.sleep(4)
        self.lp.enter_email_or_phone(self.email_or_phone)
        self.log.info('entering email or phone-->'+self.email_or_phone)
        self.lp.click_continue_btn()
        self.lp.enter_password(self.password)
        self.log.info('entering password-->'+self.password)
        self.lp.click_login_btn()
        self.log.info('clicking on login button')
        if self.lp.login_status()==True:
            self.driver.save_screenshot("C:\\Users\\ajayj\\PycharmProjects\\Amazon\\Screenshots\\amazon_sc.png")
            self.lp.click_menu_btn()
            time.sleep(4)
            self.log.info('clicking on menu button')
            self.lp.click_logout_btn()
            self.log.info('clicking on logout button')
            self.log.info('test_login_001 is passed')
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\ajayj\\PycharmProjects\\Amazon\\Screenshots\\amazon_sc.png")
            self.log.info('test_login_001 is failed')
            assert False
        self.driver.close()
        self.log.info('test_login_001 is completed')