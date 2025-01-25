from DemowebShop.library.basepage import Base


class ShoesPage(Base):

    handbag=("xpath","//a[@href='/genuine-leather-handbag-with-cell-phone-holder-many-pockets']/parent::h2")
    add_2_cart=("id","add-to-cart-button-29")
    close=("xpath","//span[@title='Close']")

    def click_handbag(self):
        self.click_on_element(self.handbag)
        self.click_on_element(self.add_2_cart)
        self.accept_alert()
        self.click_on_element(self.close)


