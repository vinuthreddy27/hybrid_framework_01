from DemowebShop.POM.homepage import HomePage


def test_shoppingcart(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_login_link()
    login_page.login_into_application()
    books_page=homepage.click_on_books()
    books_page.click_on_book1()
    homepage.click_on_shopping_cart()
    homepage.click_on_logout()
    assert homepage.message()
