from DemowebShop.POM.camcoder_page import CamcoderPage
from DemowebShop.POM.product_page import ProductResult
from DemowebShop.library.basepage import Base


class CameraPhotoPage(Base):

    hard_drive_60gb=("xpath","//a[.='1MP 60GB Hard Drive Handycam Camcorder']")
    camorader_link=("xpath","//a[.='Camcorder']")


    def click_hard_drive(self):
        self.click_on_element(self.hard_drive_60gb)

        product_page=ProductResult(self.driver)
        return product_page

    def click_on_camorader(self):
        self.click_on_element(self.camorader_link)

        carmoder_page=CamcoderPage(self.driver)
        return carmoder_page
