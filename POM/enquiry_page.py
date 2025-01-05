from DemowebShop.library.basepage import Base


class ContactUsPage(Base):

    enquiry_textfield_locator = ("id", "Enquiry")
    submit_btn_locator = ("xpath", "//input[@name='send-email']")
    messsage=("xpath","//div[@class='result']")



    def send_an_query(self):
        self.send_keys_to_element(self.enquiry_textfield_locator,"some of the product has no add to cart button")
        self.click_on_element(self.submit_btn_locator)

    def success_msg(self):
        return self.display_status(self.messsage)