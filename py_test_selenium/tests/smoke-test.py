import pytest_html
import pytest

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.home_page import HomePage
from page_objects.register_page import RegisterPage
from page_objects.account_info import AccountInfo



def test_open_url(getdriver):
      homePage = HomePage(getdriver)
      homePage.clickSignIn()
      homePage.typeEmail()

      registerPage = RegisterPage(getdriver)
      registerPage.selectGender()
      registerPage.populateUserInfo()
      registerPage.selectDateOfBirth()
      registerPage.clickSubmitReg()


      accountPage = AccountInfo(getdriver)
      accountPage.checkAlertMessage

 
#     read_data = pd.read_csv("users.csv")

#     first_name_field = DriverSetup.driver.find_element(By.ID, 'customer_firstname')
#     first_name_field.send_keys(read_data["FirstName"])

#     last_name_field = DriverSetup.driver.find_element(By.ID, 'customer_lastname')
#     last_name_field.send_keys(read_data["LastName"])

#     #email_field = driver.find_element(By.ID, 'email')
#     #email_field.send_keys(read_data["Email"])

#     password_field = driversetup.DriverSetup.find_element(By.ID, 'passwd')
#     password_field.send_keys(read_data['Password'])

#     days = driversetup.DriverSetup.find_element(By.XPATH, "//select[@id='days']/option[@value = '1']")
#     days.click()

#     months = driversetup.DriverSetup.find_element(By.XPATH, "//select[@id='months']/option[@value='2']")
#     months.click()

#     years = driversetup.DriverSetup.find_element(By.XPATH, "//select[@id='years']/option[@value='1992']")
#     years.click()

#     submit_button = driversetup.DriverSetup.find_element(By.XPATH, '//button[@id="submitAccount"]')
#     submit_button.click()

#     alert_success = driversetup.DriverSetup.find_element(By.XPATH, "//p[@class = 'alert alert-success']")
    
#     assert alert_success.is_displayed()
#     sleep(5)





# def tear_down():
#     driversetup.DriverSetup.closeBrowser()