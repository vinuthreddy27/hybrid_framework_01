from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,7)
        self.actions=ActionChains(self.driver)


    def click_on_element(self,locator):
        element=self.wait.until(presence_of_element_located((locator)))
        element.click()

    def send_keys_to_element(self, locator,text):
        element = self.wait.until(presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)


    def visiblity(self,locator):
        element=self.wait.until(visibility_of_element_located(locator))
        return element

    def hover(self,locator):
        element=self.wait.until(presence_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    def driver_back(self):
        self.driver.back()

    def driver_forward(self):
        self.driver.forward()

    def driver_refresh(self):
        self.driver.refresh()

    def display_status(self,locator):
        element=self.wait.until(visibility_of_element_located(locator))
        return element.is_displayed()