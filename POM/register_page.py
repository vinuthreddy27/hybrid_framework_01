from DemowebShop.library.basepage import Base


class RegisterPage(Base):

    male_radio_btn = ("id", "gender-male")
    female_radio_btn = ("id", "gender-female")
    first_name_locator = ("id", "FirstName")
    last_name_locator = ("id", "LastName")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    conform_password_locator = ("id", "ConfirmPassword")
    register_btn = ("id", "register-button")
    continue_btn = ("xpath", "//input[@value='Continue']")

    def register_into_application(self,fn,ln,mail,password,cp):
        self.click_on_element(self.female_radio_btn)
        self.send_keys_to_element(self.first_name_locator,fn)
        self.send_keys_to_element(self.last_name_locator,ln)
        self.send_keys_to_element(self.email_locator,mail)
        self.send_keys_to_element(self.password_locator,password)
        self.send_keys_to_element(self.conform_password_locator,cp)
        self.click_on_element(self.register_btn)
        self.click_on_element(self.continue_btn)
