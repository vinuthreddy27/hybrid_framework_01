from DemowebShop.library.basepage import Base


class ProductResult(Base):

    compare_btn=("xpath","//*[@value='Add to compare list']")

    def click_on_compareBtn(self):
        self.click_on_element(self.compare_btn)
        self.driver_back()
        self.driver_back()


