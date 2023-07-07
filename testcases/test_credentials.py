import time

from pageObject.loginPage import loginpage
from utilities.logger import LogJenerator
from utilities.readproperties import readconfig

class Test_credentials_login:
    url=readconfig.geturl()
    log=LogJenerator.loggen()


    def test_credentials_login_001(self,setup,getDataforlogin):
        self.driver=setup
        self.lp=loginpage(self.driver)
        self.log.info('login test case started')
        self.log.info('opening browser')
        self.driver.get(self.url)
        self.log.info('go to this url-->'+self.url)
        self.lp.click_signin_dashboard()
        time.sleep(4)
        self.lp.enter_email_or_phone(getDataforlogin[0])
        self.log.info('entering email_or_phone-->'+getDataforlogin[0])
        self.lp.click_continue_btn()
        self.lp.enter_password(getDataforlogin[1])
        self.log.info('entering password-->'+getDataforlogin[1])
        self.lp.click_login_btn()
        self.log.info('clicking on login button')
        if self.lp.login_status()==True:
            if getDataforlogin[2] == 'pass':
                self.lp.click_menu_btn()
                time.sleep(4)
                self.log.info('clicking on menu button')
                self.lp.click_logout_btn()
                self.log.info('clicking on logout button')
                self.log.info('test_login_001 is passed')
                assert True
            else:
                assert False
        else:
            if getDataforlogin[2] == 'fail':
                self.log.info('test case is passed')
                assert True
            else:
                assert False
        self.driver.close()
        self.log.info('test case completed')


