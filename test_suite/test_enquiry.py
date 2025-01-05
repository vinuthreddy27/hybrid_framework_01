from DemowebShop.POM.homepage import HomePage


def test_enquiry(get_browser):
    homepage=HomePage(get_browser)
    login_page=homepage.click_login_link()
    login_page.login_into_application()
    contacts_page=homepage.click_on_contacts_link()
    contacts_page.send_an_query()
    assert contacts_page.success_msg()