from DemowebShop.POM.changePassword_page import PasswordChange
from DemowebShop.library.basepage import Base


class MyaccountPage(Base):

    change_password_locator = ("xpath", "//a[.='Change password']")


    def click_on_change_password(self):
        self.click_on_element(self.change_password_locator)

        passwordchange_page=PasswordChange(self.driver)
        return passwordchange_page