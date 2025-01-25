

from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located, \
    alert_is_present
from selenium.webdriver.support.select import Select
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

    def scroll(self,x,y):
        self.actions.scroll_by_amount(x,y).perform()

    def select_an_option(self,locator,value):
        dropdown=self.wait.until(presence_of_element_located(locator))
        s1=Select(dropdown)
        s1.select_by_visible_text(value)

    def select_an_by_index(self, locator, index):
        dropdown = self.wait.until(presence_of_element_located(locator))
        s1 = Select(dropdown)
        s1.select_by_index(index)

    def get_text(self,locator):
        element=self.wait.until(visibility_of_element_located(locator))
        print(element.text)

    def accept_alert(self):
        element = self.wait.until(alert_is_present())
        element.accept()

    def dismiss_alert(self):
        element=self.driver.switch_to.alert
        element.accept()