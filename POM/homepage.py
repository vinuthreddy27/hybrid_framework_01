from DemowebShop.POM.camera_photo_page import CameraPhoto
from DemowebShop.POM.loginpage import LoginPage
from DemowebShop.POM.register_page import RegisterPage
from DemowebShop.library.basepage import Base


class HomePage(Base):

    register_link=("css selector","a[href='/register']")
    login_link=("xpath","//a[.='Log in']")
    electronics_link=("xpath","//ul[@class='top-menu']//a[@href='/electronics']")
    camera_option=("xpath","//ul[@class='top-menu']//a[@href='/camera-photo']")

    logout_link=("xpath","//a[.='Log out']")


    def click_register_link(self):
        self.click_on_element(self.register_link)

        register_page=RegisterPage(self.driver)
        return register_page

    def click_login_link(self):
        self.click_on_element(self.login_link)

        login_page = LoginPage(self.driver)
        return login_page

    def hover_onto_electronics(self):
        self.hover(self.electronics_link)
        self.click_on_element(self.camera_option)

        cameraPhoto_page=CameraPhoto(self.driver)
        return cameraPhoto_page

    def click_on_logout(self):
        self.click_on_element(self.logout_link)

    def proper_msg(self):
        self.display_status(self.login_link)