from DemowebShop.library.basepage import Base


class ReviewPage(Base):

    review_title_locator = ("id", "AddProductReview_Title")

    review_text_locator = ("id", "AddProductReview_ReviewText")

    rating_locator = ("xpath", "//input[@value='4']")

    submit_locator = ("name", "add-review")