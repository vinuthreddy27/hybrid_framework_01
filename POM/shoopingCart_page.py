from DemowebShop.library.basepage import Base


class ShoppingPage(Base):

    quantity_locator = ("xpath", "//input[@class='qty-input']")

    remove_cart_locator = ("xpath", "//td[@class='remove-from-cart']")

    update_cart_locator = ("name", "updatecart")