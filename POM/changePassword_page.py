from DemowebShop.library.basepage import Base


class PasswordChange(Base):

    change_password_locator = ("xpath", "//a[.='Change password']")
    old_password_locator = ("name", "OldPassword")
    new_password_locator = ("name", "NewPassword")
    conform_password_locator = ("id", "ConfirmNewPassword")
    change_password_btn = ("xpath", "//input[@value='Change password']")

    message=("xpath","//div[@class='result']")



    def change_password(self):
        self.send_keys_to_element(self.old_password_locator,"selenium")
        self.send_keys_to_element(self.new_password_locator,"selenium")
        self.send_keys_to_element(self.conform_password_locator,"selenium")
        self.click_on_element(self.change_password_btn)
        self.get_text(self.message)