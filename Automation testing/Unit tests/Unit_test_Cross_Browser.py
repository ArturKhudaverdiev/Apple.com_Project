# Cross-Browser test with Chrome, FireFox and Edge. 3 same tests for each Browser

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
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException as WDE


# GoogleChrome Browser UnitTest HOME PAGE:

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

    #Check that the main Apple logotype is visible and clickable (TC - 001)

    def test_main_logotype(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.store)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.store)))
        print("The main Apple logotype is visible and clickable")


    #Check that the top menu is visible and clickable (TC - 002)
    def test_top_menu(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.store)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.store)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.mac)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.mac)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.ipad)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.ipad)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.iphone)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.iphone)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.watch)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.watch)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.vision)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.vision)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.airpods)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.airpods)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.tv_home)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.tv_home)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.entertainment)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.entertainment)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.accessories)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.accessories)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.support)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.support)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.search)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.search)))
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.bag)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.bag)))
        time.sleep(2)
        print("The top menu is visible and clickable")

    #Check that in the home page Carusel is work correct (TC - 003)
    def test_carousel(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)
        driver.find_element(By.XPATH, hp.carousel1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel2).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel3).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel4).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel5).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel6).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel7).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel8).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel9).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel10).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel11).click()
        time.sleep(1)
        driver.find_element(By.XPATH, hp.carousel12).click()
        time.sleep(1)
        print("The Carousel is work correct")

    #Check that the footer menu in home page is visible and clickable (TC - 004)
    def test_footer_menu(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        try:
            # Shop and Learn
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_store)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_store)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_i_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_i_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_vision)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_vision)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_air_pods)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_air_pods)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_tv_home)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_tv_home)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_air_tag)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_air_tag)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_accessories)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_gift_cards)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_gift_cards)))
            time.sleep(2)

            # Apple Wallet
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_wallet)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_wallet)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_card)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_card)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_pay)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_pay)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_cash)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_cash)))
            time.sleep(2)

            # Account
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_manage_your_apple_id)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_manage_your_apple_id)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_store_account)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_store_account)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_i_cloud_id)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_i_cloud_id)))
            time.sleep(2)

            # Entertainment
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_one)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_one)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_tv)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_tv)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_music)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_music)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_arcade)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_arcade)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_fitness)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_fitness)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_news)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_news)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_podcasts)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_podcasts)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_books)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_books)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_app_store)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_app_store)))
            time.sleep(2)

            # Apple Store
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_find_a_store)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_find_a_store)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_genius_bar)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_genius_bar)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_today_at_apple)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_today_at_apple)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_camp)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_camp)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_store_app)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_store_app)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_certified_refurbished)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_certified_refurbished)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_trade_in)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_trade_in)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_financing)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_financing)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_carrier_deals_at_apple)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_carrier_deals_at_apple)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_order_status)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_order_status)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.shopping_help)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.shopping_help)))
            time.sleep(2)

            # For Business
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_and_business)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_and_business)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_shop_for_business)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_shop_for_business)))
            time.sleep(2)

            # For Education
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_and_education)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_and_education)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_shop_for_k12)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_shop_for_k12)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_shop_for_college)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_shop_for_college)))
            time.sleep(2)

            # For Healthcare
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_in_healthcare)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_in_healthcare)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_health_on_apple_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_health_on_apple_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_health_records_on_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_health_records_on_iphone)))
            time.sleep(2)

            # For Government
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_shop_for_government)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_shop_for_government)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_shop_for_veterans_and_military)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_shop_for_veterans_and_military)))
            time.sleep(2)

            # Apple Values
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_accessibility)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_accessibility)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_education)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_education)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_environment)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_environment)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_inclusion_and_diversity)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_inclusion_and_diversity)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_privacy)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_privacy)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_racial_equity_and_justice)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_racial_equity_and_justice)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_supplier_responsibility)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_supplier_responsibility)))
            time.sleep(2)

            # About apple
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_newsroom)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_newsroom)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_apple_leadership)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_apple_leadership)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_career_opportunities)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_career_opportunities)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_investors)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_investors)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_ethics_and_compliance)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_ethics_and_compliance)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_events)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_events)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_contact_apple)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_contact_apple)))
            time.sleep(2)

            # Copyright © 2023 Apple Inc. All rights reserved.
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_privacy_policy)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_privacy_policy)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_terms_of_use)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_terms_of_use)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_sales_and_refunds)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_sales_and_refunds)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_legal)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_legal)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_site_map)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_site_map)))
            time.sleep(2)

            # Footer choose country
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.f_country)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.f_country)))
            time.sleep(2)
        except TimeoutException:
            print("The footer menu is visible and clickable")

    # Verify that in submenu on top menu is visible and clickable (TC - 005)
    def test_drop_down_top_menu(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        try:
            # Shop
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_the_latest)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_the_latest)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_accessories)))

            # Quick links
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_find_a_store)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_find_a_store)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_order_status)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_order_status)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_trade_in)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_trade_in)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_financing)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_financing)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_college_student_offer)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_college_student_offer)))

            # Shop Special Stores
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_certified_refurbished)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_certified_refurbished)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_education)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_education)))

        except TimeoutException:
            print("The drop down menu is clickable")





















