from DemowebShop.POM.loginpage import LoginPage
from DemowebShop.POM.register_page import RegisterPage
from DemowebShop.library.basepage import Base


class HomePage(Base):

    register_link=("css selector","a[href='/register']")
    login_link=("xpath","//a[.='Log in']")
    electronics_link=("xpath","//a[text()='Electronics']")
    camera_option=("xpath","//ul[@class='top-menu']//a[@href='/camera-photo']")


    def click_register_link(self):
        self.click_on_element(self.register_link)

        register_page=RegisterPage(self.driver)
        return register_page

    def click_login_link(self):
        self.click_on_element(self.login_link)

        login_page = LoginPage(self.driver)
        return login_page

    def move_to_photo(self):
        self.hover_on_an_element(self.electronics_link)
        self.click_on_element(self.camera_option)

