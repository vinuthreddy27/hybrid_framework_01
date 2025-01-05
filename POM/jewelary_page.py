from DemowebShop.library.basepage import Base


class JewelaryPage(Base):
    price1=("xpath","//*[@href='https://demowebshop.tricentis.com/jewelry?price=0-500']")
    black_diamond=("xpath","//*[@href='/black-white-diamond-heart']")


    def clcik_on_price1(self):
        self.click_on_element(self.price1)

    def click_on_diamond(self):
        self.click_on_element(self.black_diamond)