from DemowebShop.POM.product_page import ProductResult
from DemowebShop.library.basepage import Base


class CameraPhoto(Base):
    hard_drive_60gb=("xpath","//a[.='1MP 60GB Hard Drive Handycam Camcorder']")
    camorader_link=("xpath","//a[.='Camcorder']")


    def click_hard_drive(self):
        self.click_on_element(self.hard_drive_60gb)

        product_page=ProductResult(self.driver)
        return product_page

