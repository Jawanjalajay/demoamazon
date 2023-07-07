import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver=webdriver.Edge()
    # driver.implicitly_wait(5)
    # driver.maximize_window()
    # driver.get("https://www.amazon.in/")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print('launching chrome')
    elif browser=='edge':
        driver=webdriver.Edge()
        print('launching edge')
    else:
        print('Headless mode')
        edge_options=webdriver.EdgeOptions()
        edge_options.add_argument('headless')
        driver=webdriver.Edge(options=edge_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


def pytest_metadata(metadata):
    metadata['environment']='Test'
    metadata['project name']='Amazon'
    metadata['module name']='Login'
    metadata['Tester']="Ajay"
    metadata.pop('Plugins',None)
    metadata.pop('Packages',None)

@pytest.fixture(params=[
    ('8668237241','Ajay@1234','pass'),
    ('0668237241','Ajay@1234','fail'),
    ('8668237241','Ajay@1230','fail'),
    ('0668237241','Ajay@1230','fail')

])

def getDataforlogin(request):
    return request.param