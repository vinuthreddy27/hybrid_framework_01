from DemowebShop.library.basepage import Base


class ComparePage(Base):

    remove_btn=("xpath","//img[@alt='Picture of Camcorder']/../..//input")
    remove_btn2=("xpath","//img[@alt='Picture of 1MP 60GB Hard Drive Handycam Camcorder']/../../..//input")


    def click_on_removeBtn(self):
        self.click_on_element(self.remove_btn)


    def click_on_removeBtn2(self):
        self.click_on_element(self.remove_btn2)


