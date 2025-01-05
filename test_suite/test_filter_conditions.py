from DemowebShop.POM.homepage import HomePage


def test_Filterconditions(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_login_link()
    login_page.login_into_application()
    dekstop_page=homepage.hover_on_computers()
    dekstop_page.select_option_from_Dropdown1()
    dekstop_page.select_option_from_Dropdown2()
    dekstop_page.click_on_filterprice()
    homepage.click_on_logout()
    assert homepage.message()
