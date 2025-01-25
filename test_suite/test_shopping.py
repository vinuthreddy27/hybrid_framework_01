from DemowebShop.POM.homepage import HomePage


def test_shopping_conditions(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_login_link()
    login_page.login_into_application()
    shoes_page=homepage.click_on_shoes()
    shoes_page.click_handbag()
    homepage.click_on_shopping_cart()
    assert homepage.out_of_Stock_msg()