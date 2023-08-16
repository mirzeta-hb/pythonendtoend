import pytest
from selenium import webdriver

driver: webdriver

@pytest.fixture(scope='class')
def getdriver():
    driver = webdriver.Chrome()
    driver.get("http://www.automationpractice.pl/index.php")
    yield driver


    def closeBrowser(self):
       self.driver.close()
