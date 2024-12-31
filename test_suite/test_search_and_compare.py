from DemowebShop.POM.homepage import HomePage


def test_compare(get_browser):
    homepage = HomePage(get_browser)
    login_page = homepage.click_login_link()
    login_page.login_into_application()
    camera_page = homepage.hover_onto_electronics()
    prductcamera_page.click_hard_drive()
