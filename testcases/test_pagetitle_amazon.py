import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_pagetitle():
    @pytest.mark.skip
    def test_pageTitle_001(self):

        driver=webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.in/")
        if self.driver.find_element(By.ID,"nav-logo-sprites").is_displayed():
            assert True
        else:
            assert False
