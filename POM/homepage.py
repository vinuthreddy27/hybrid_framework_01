from DemowebShop.POM.books_page import BooksPage
from DemowebShop.POM.camera_photo_page import  CameraPhotoPage
from DemowebShop.POM.dekstop_page import DekstopPage
from DemowebShop.POM.enquiry_page import ContactUsPage
from DemowebShop.POM.loginpage import LoginPage
from DemowebShop.POM.myaccountpage import MyaccountPage
from DemowebShop.POM.register_page import RegisterPage
from DemowebShop.POM.shoopingCart_page import ShoppingPage
from DemowebShop.library.basepage import Base


class HomePage(Base):

    register_link=("css selector","a[href='/register']")

    login_link=("xpath","//a[.='Log in']")

    electronics_link=("xpath","//ul[@class='top-menu']//a[@href='/electronics']")

    camera_option=("xpath","//ul[@class='top-menu']//a[@href='/camera-photo']")

    logout_link=("xpath","//a[.='Log out']")

    search_textfield=("id","small-searchterms")

    search_btn=("xpath","//input[@value='Search']")

    shopping_cart=("xpath","//*[.='Shopping cart']")

    books_link=("xpath","//ul[@class='top-menu']//a[@href='/books']")

    contact_us_locator = ("xpath", "//a[.='Contact us']")

    computers_link=("xpath","//ul[@class='top-menu']//*[@href='/computers']")

    dekstop_link=("xpath","//ul[@class='top-menu']//a[@href='/desktops']")

    my_account_link=("xpath","//a[.='My account']")

    jewelary_link=("xpath","//ul[@class='top-menu']//a[@href='/jewelry']")

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

        cameraPhoto_page=CameraPhotoPage(self.driver)
        return cameraPhoto_page

    def click_on_logout(self):
        self.click_on_element(self.logout_link)

    def proper_msg(self):
        self.display_status(self.login_link)


    def search_product(self,value):
        self.send_keys_to_element(self.search_textfield,value)
        self.click_on_element(self.search_btn)


    def click_on_books(self):
        self.click_on_element(self.books_link)

        books_page=BooksPage(self.driver)
        return books_page

    def click_on_shopping_cart(self):
        self.click_on_element(self.shopping_cart)

        shoppingcart_page=ShoppingPage(self.driver)
        return shoppingcart_page

    def hover_on_computers(self):
        self.hover(self.computers_link)
        self.click_on_element(self.dekstop_link)

        dekstop_page=DekstopPage(self.driver)
        return dekstop_page


    def click_on_myaccount(self):
        self.scroll(50,100)
        self.click_on_element(self.my_account_link)

        accountpage=MyaccountPage(self.driver)
        return accountpage

    def click_on_contacts_link(self):
        self.click_on_element(self.contact_us_locator)

        contacts_page=ContactUsPage(self.driver)
        return contacts_page

    def message(self):
        return self.display_status(self.login_link)

    def click_on_jewelary(self):
        self.click_on_element(self.jewelary_link)