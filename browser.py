from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser(object):
    base_url = 'https://'
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)

    def find_by_xpath(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_xpath(selector)
