from page_objects.common_ops import CommonOps, findByXpath , findById, wait_for
import pandas as pd
from selenium.webdriver.common.by import By


class RegisterPage(CommonOps): 

    gender_field = (By.XPATH, "//input[@id= 'id_gender2']")
    first_name = 'customer_firstname'
    last_name = 'customer_lastname'
    email = 'email'
    password = 'passwd'
    day = "//select[@id='days']/option[@value = '1']"
    month = "//select[@id='months']/option[@value='2']"
    year = "//select[@id='years']/option[@value='1992']"
    submit_button = "//button[@id='submitAccount']"

    def __init__(self, driver):
        super().__init__(driver)


    def selectGender(self):
     gender = wait_for(self, self.gender_field)
     gender.click()


    def populateUserInfo(self):
       read_data = pd.read_csv("users.csv")
       name = findById(self, self.first_name)
       name.send_keys(read_data["FirstName"])

       lname = findById(self, self.last_name)
       lname.send_keys(read_data["LastName"])

       password = findById(self, self.password)
       password.send_keys(read_data["Password"])


    def selectDateOfBirth(self):
       dayOfB = findByXpath(self, self.day)
       dayOfB.click()

       monthOfB = findByXpath(self, self.month)
       monthOfB.click()
       
       yearOfB = findByXpath(self, self.year)
       yearOfB.click()

    def clickSubmitReg(self):
       submit = findByXpath(self, self.submit_button)
       submit.click()