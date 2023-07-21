#Verify that all country is visible and clickable

from selenium import webdriver
import random
import time
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import helpers as hp
from selenium.webdriver.support import expected_conditions as EC

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    #Check that the current url is correct

        driver2 = self.driver
        driver2.get(hp.url)
        time.sleep(2)

        # Random delay function:
        def delay():
            time.sleep(random.randint(1, 5))
            delay()

        Apple_Expected_Url = hp.url
        current_url = driver2.current_url
        if current_url == Apple_Expected_Url:
            print("The currect URL is correct:", driver2.current_url)
        else:
            print("The current url is error:", driver2.current_url)

        # Check that the Apple title is correct
        Apple_Expected_Title = "Apple"
        current_title = driver2.title
        if Apple_Expected_Title == current_title:
            print("The Apple TITLE is correct:", driver2.title)
        else:
            print("The Apple TITLE is error:", driver2.title)

    def test_Africa_Middle_East_and_India(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located())

