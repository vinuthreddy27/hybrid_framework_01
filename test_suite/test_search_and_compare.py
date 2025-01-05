from DemowebShop.POM.homepage import HomePage


def test_compare(get_browser):
    homepage = HomePage(get_browser)
    login_page = homepage.click_login_link()
    login_page.login_into_application()
    cameraPhoto_page = homepage.hover_onto_electronics()
    product_page=cameraPhoto_page.click_hard_drive()
    product_page.click_on_compareBtn()
    camcoder_page=cameraPhoto_page.click_on_camorader()
    compare_page=camcoder_page.click_on_compare_btn()
    compare_page.click_on_removeBtn()
    compare_page.click_on_removeBtn2()
    homepage.click_on_logout()
    assert homepage.message()

    