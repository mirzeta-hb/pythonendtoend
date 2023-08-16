from page_objects.common_ops import CommonOps, findByXpath
from selenium.webdriver.support import expected_conditions as EC


class AccountInfo(CommonOps):   
    alert_message = "//p[@class = 'alert alert-success']"

    def __init__(self, driver):
        super().__init__(driver)



    def checkAlertMessage(self):
     alert = findByXpath(self, self.alert_message)
     assert alert.is_displayed()
