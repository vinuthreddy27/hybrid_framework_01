from DemowebShop.POM.homepage import HomePage


def test_Review(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_login_link()
    login_page.login_into_application()