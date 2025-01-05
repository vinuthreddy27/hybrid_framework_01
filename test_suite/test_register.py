import pytest

from DemowebShop.POM.homepage import HomePage
from DemowebShop.utilities.excel_reader import get_data_from_excel


@pytest.mark.parametrize("fn,ln,mail,password,cp",get_data_from_excel("C:/Users/Vinuthreddy/Documents/Book8.xlsx","Sheet1"))
def test_register(get_browser,fn,ln,mail,password,cp):
    homepage=HomePage(get_browser)
    register_page=homepage.click_register_link()
    register_page.register_into_application(fn,ln,mail,password,cp)