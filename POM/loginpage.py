from DemowebShop.configurations.config import TestData
from DemowebShop.library.basepage import Base


class LoginPage(Base):
    email=("css selector","#Email")
    password=("xpath","//input[@name='Password']")
    login_btn=("xpath","//button[@value='Log in']")


    def login_into_application(self):
        self.send_keys_to_element(self.email, TestData.email)
        self.send_keys_to_element(self.password, TestData.password)
        self.click_on_element(self.login_btn)