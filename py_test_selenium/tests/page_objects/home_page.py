from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from page_objects.common_ops import CommonOps, findById, findByXpath


class HomePage(CommonOps):

   sign_in_button = (By.XPATH, "//div[@class='header_user_info']/a")
   input_email_field = 'email_create'
   submit_button = 'SubmitCreate'
   

   def __init__(self, driver):
       super().__init__(driver)

   def clickSignIn(self):
       el = self._wait.until(ec.presence_of_element_located(self.sign_in_button))
       el.click()

   def typeEmail(self):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%m/%d/%Y%H%M%S")
        email = f"{current_time}email1@hotmail.com"
        element = findById(self, self.input_email_field)
        element.send_keys(email)

        submit = findById(self, self.submit_button)
        submit.click()


        


