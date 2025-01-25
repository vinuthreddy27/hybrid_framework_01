from DemowebShop.POM.homepage import HomePage


def test_login(get_browser):
    homepage = HomePage(get_browser)
    login_page = homepage.click_login_link()
    login_page.login_into_application()
    homepage.click_on_logout()


