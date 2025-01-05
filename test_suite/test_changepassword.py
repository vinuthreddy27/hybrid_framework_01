from DemowebShop.POM.homepage import HomePage


def test_change_password(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_login_link()
    login_page.login_into_application()
    accountpage=homepage.click_on_myaccount()
    passwordchange_page=accountpage.click_on_change_password()
    passwordchange_page.change_password()
    homepage.click_on_logout()
    assert homepage.message()