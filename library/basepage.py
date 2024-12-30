from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class Base:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,6,poll_frequency=3)
        self.actions=ActionChains(self.driver)


    def click_on_element(self,locator):
        element=self.wait.until(presence_of_element_located(locator))
        element.click()

    def send_keys_to_element(self, locator,text):
        element = self.wait.until(presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def hover_on_an_element(self,locator):
        self.actions.move_to_element(locator).perform()
