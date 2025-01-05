from DemowebShop.library.basepage import Base


class DekstopPage(Base):

    dropdown_1=("id","products-orderby")
    dropdown_2=("id","products-pagesize")
    filter_price=("xpath","//ul[@class='price-range-selector']//a[contains(.,'Under')]//span")
    price2=("xpath","//ul[@class='price-range-selector']//li[2]/a")
    price3=("xpath","//ul[@class='price-range-selector']//li[3]/a")
    remover_filter_link=("xpath","//*[.='Remove Filter']")



    def select_option_from_Dropdown1(self):
        self.select_an_by_index(self.dropdown_1,0)
        self.select_an_by_index(self.dropdown_1, 1)
        self.select_an_by_index(self.dropdown_1, 2)
        self.select_an_by_index(self.dropdown_1, 3)


    def select_option_from_Dropdown2(self):
        self.select_an_by_index(self.dropdown_2,0)
        self.select_an_by_index(self.dropdown_2, 1)
        self.select_an_by_index(self.dropdown_2, 2)


    def click_on_filterprice(self):
        self.click_on_element(self.filter_price)
        self.click_on_element(self.remover_filter_link)
        self.click_on_element(self.price2)
        self.click_on_element(self.remover_filter_link)
        self.click_on_element(self.price3)
        self.click_on_element(self.remover_filter_link)