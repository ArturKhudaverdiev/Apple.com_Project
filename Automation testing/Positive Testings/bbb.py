# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAppleSeleniumIDE():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_appleSeleniumIDE(self):
        self.driver.get("https://www.apple.com/")
        self.driver.set_window_size(1536, 815)
        self.driver.find_element(By.LINK_TEXT, "Buy").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#f5728b51-36d6-11ee-902e-2526dacf655c_label .price-point > span > .nowrap:nth-child(1)").click()
        self.driver.execute_script("window.scrollTo(0,604.4444580078125)")
        self.driver.find_element(By.CSS_SELECTOR, ".colornav-item:nth-child(1) .colornav-swatch").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#f5730080-36d6-11ee-902e-2526dacf655c_label .nowrap:nth-child(1) > span:nth-child(1)").click()
        self.driver.find_element(By.ID, "noTradeIn_label").click()
        self.driver.find_element(By.ID, "fd436de0-36d6-11ee-902e-2526dacf655c_label").click()
        self.driver.find_element(By.ID, "f5739cc0-36d6-11ee-902e-2526dacf655c_label").click()
        self.driver.find_element(By.ID, "applecareplus_59_noapplecare_label").click()
        self.driver.find_element(By.NAME, "add-to-cart").click()
        element = self.driver.find_element(By.NAME, "add-to-cart")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.NAME, "proceed").click()

