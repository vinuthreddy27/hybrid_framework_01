from DemowebShop.library.basepage import Base


class BooksPage(Base):

    book1=("xpath","//img[contains(@src,'computing-and-internet_125.jpeg')]")
    cart_btn=("id","add-to-cart-button-13")


    def click_on_book1(self):
        self.scroll(110,150)
        self.click_on_element(self.book1)
        self.click_on_element(self.cart_btn)