import pytest
from selenium import webdriver
from DemowebShop.configurations.config import TestData


@pytest.fixture(params=["chrome","firefox","edge"],scope="function")
def get_browser(request):
    global driver
    if request.param=="chrome":
        driver=webdriver.Chrome()

    elif request.param=="edge":
        driver=webdriver.Edge()

    elif request.param=="firefox":
        driver=webdriver.Firefox()

    else:
        print("provide valid browser")

    driver.get(TestData.base_url)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(6)
    yield
    driver.quit()