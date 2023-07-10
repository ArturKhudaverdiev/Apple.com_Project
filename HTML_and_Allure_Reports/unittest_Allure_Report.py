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
import AllureReports



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
        print("The main Apple logotype is visible and clickable. TC - 001 IS PASSED")


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
        print("The top menu is visible and clickable. TC - 002 IS PASSED")

        #Check that the search icon is click and visible (TC-003)
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.search)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.search)))
        print("The search icon is visible and clickable. TC - 003 IS PASSED")

        # Check that the bag icon is click and visible (TC-004)
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.bag)))
        wait.until(EC.element_to_be_clickable((By.XPATH, hp.bag)))
        time.sleep(2)
        print("The bag icon is visible and clickable. TC - 004 IS PASSED")

    #Check that in the home page Carusel is work correct (TC - 005)
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
        print("The Carousel is work correct. TC - 005 IS PASSED")

    #Check that the footer menu in home page is visible and clickable (TC - 006)
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
            print("The footer menu is visible and clickable. TC - 006 IS PASSED")

    # Verify that in submenu on top menu is visible and clickable (TC - 007)
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
            time.sleep(2)

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
            time.sleep(2)

            # Shop Special Stores
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_certified_refurbished)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_certified_refurbished)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_education)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_education)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_business)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_business)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_veterans_and_military)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_veterans_and_military)))
            time.sleep(2)

            # MAC
            # Explore Mac
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_all_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_all_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_macbook_air)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_macbook_air)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_macbook_pro)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_macbook_pro)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_i_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_i_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_mini)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_mini)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_studio)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_studio)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_pro)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_pro)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_displays)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_displays)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_compare_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_compare_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_does_that)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_does_that)))
            time.sleep(2)

            # Shop Mac
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_accessories)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_trade_in_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_trade_in_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_financing_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_financing_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_college_student_offer_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_college_student_offer_mac)))
            time.sleep(2)

            # More from Mac
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_macos_sonoma_preview)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_macos_sonoma_preview)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_final_cut_pro)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_final_cut_pro)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_logic_pro)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_logic_pro)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_continuity)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_continuity)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_i_cloud)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_i_cloud)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_for_business)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_for_business)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_education_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_education_mac)))
            time.sleep(2)

            # IPAD
            # Explore iPad
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_all_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_all_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_pro)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_pro)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_air)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_air)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_mini)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_mini)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_pencil)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_pencil)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_keyboards)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_keyboards)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_compare_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_compare_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_why_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_why_ipad)))
            time.sleep(2)

            #Shop iPad
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_accessories)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_trade_in_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_trade_in_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_financing_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_financing_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_college_student_offer_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_college_student_offer_ipad)))
            time.sleep(2)

            #More from iPad
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_final_cut_pro_for_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_final_cut_pro_for_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_logic_pro_for_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_logic_pro_for_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_icloud_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_icloud_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_education_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_education_ipad)))
            time.sleep(2)

            # IPHONE
            # Explore iPhone
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_all_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_all_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_compare_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_compare_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_switch_from_android)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_switch_from_android)))
            time.sleep(2)

            # Shop iPhone
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_iphone_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_iphone_accessories)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_trade_in_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_trade_in_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_carrier_deals_at_apple)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_carrier_deals_at_apple)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_financing_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_financing_iphone)))
            time.sleep(2)

            # More from Iphone
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_iphone_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_iphone_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_iphone_privacy)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_iphone_privacy)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_icloud_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_icloud_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_wallet_pay_card)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_wallet_pay_card)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_siri)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_siri)))
            time.sleep(2)

            # WATCH
            # Explore watch
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_all_apple_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_all_apple_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_compare_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_compare_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_why_apple_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_why_apple_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_apple_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_apple_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_watch_studio)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_watch_studio)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_watch_bands)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_watch_bands)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_watch_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_watch_accessories)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_trade_in_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_trade_in_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_financing_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_financing_watch)))
            time.sleep(2)

            # More from Watch
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_watch_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_watch_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_fitness)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_fitness)))
            time.sleep(2)

            # AIRPODS
            # ExploreAirPods
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_all_airpods)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_all_airpods)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_compare_airpods)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_compare_airpods)))
            time.sleep(2)

            # ShopAirPods
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_airpods)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_airpods)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_airpods_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_airpods_accessories)))
            time.sleep(2)

            # More from AirPods
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_airpods_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_airpods_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_music)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_music)))
            time.sleep(2)

            # TV AND HOME
            # Explore TV & Home
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_tv_home)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_tv_home)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_tv_4k)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_tv_4k)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_homepod)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_homepod)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_homepod_mini)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_homepod_mini)))
            time.sleep(2)

            # Shop TV & Home
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_apple_tv_4k)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_apple_tv_4k)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_homepod)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_homepod)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_homepod_mini)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_homepod_mini)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_siri_remote)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_siri_remote)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_tv_home_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_tv_home_accessories)))
            time.sleep(2)

            # More from TV & Home
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_tv_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_tv_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_homepod_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_homepod_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_tv_app)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_tv_app)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_tv_plus)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_tv_plus)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_home_app)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_home_app)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_music_tv_home)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_music_tv_home)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_siri_tv_home)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_siri_tv_home)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_airplay)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_airplay)))
            time.sleep(2)

            # ENTERTAINMENT
            # Explore entertainment
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_entertainment)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_entertainment)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_one)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_one)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_tv_plus_entertainment)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_tv_plus_entertainment)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_music_entertainment)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_music_entertainment)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_arcade)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_arcade)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_fitness_entertainment)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_fitness_entertainment)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_news_plus)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_news_plus)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_podcasts)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_podcasts)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_books)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_books)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_app_store)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_app_store)))
            time.sleep(2)

            # Support
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_tv_plus_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_tv_plus_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_music_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_music_support)))
            time.sleep(2)

            # ACCESSORIES
            # Shop Accessories
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_all_accessories)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_all_accessories)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_accessories_mac)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_accessories_mac)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_accessories_ipad)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_accessories_ipad)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_accessories_iphone)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_accessories_iphone)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_accessories_apple_watch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_accessories_apple_watch)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_accessories_air_pods)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_accessories_air_pods)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_shop_accessories_tv_home)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_shop_accessories_tv_home)))
            time.sleep(2)

            # Explore Accessories
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_made_by_apple)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_made_by_apple)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_beats_by_dr_dre)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_beats_by_dr_dre)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_air_tag)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_air_tag)))
            time.sleep(2)

            # SUPPORT
            # Explore support
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_iphone_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_iphone_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_mac_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_mac_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_ipad_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_ipad_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_watch_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_watch_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_air_pods_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_air_pods_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_music_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_music_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_tv_home_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_tv_home_explore_support)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_explore_support)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_explore_support)))
            time.sleep(2)

            # Get Help
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_community)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_community)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_check_coverage)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_check_coverage)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_repair)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_repair)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_contact_us)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_contact_us)))
            time.sleep(2)

            # Helpful topics
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_get_apple_care_plus)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_get_apple_care_plus)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_apple_id_and_password)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_apple_id_and_password)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_billing_and_subscriptions)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_billing_and_subscriptions)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_find_me)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_find_me)))
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.s_accessibility)))
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.s_accessibility)))
        except TimeoutException:
            print("The drop down menu is clickable and visible. TC - 007 IS PASSED")

    #Verify that user get valid information on search page (TC - 008)
    def test_input_search_iphone(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get(hp.url)
        time.sleep(2)

        driver.find_element(By.XPATH, hp.search).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[contains(@class,'globalnav-searchfield-input')]").send_keys("Iphone")
        time.sleep(4)
        driver.find_element(By.XPATH, "//input[contains(@class,'globalnav-searchfield-input')]").send_keys(Keys.ENTER)
        time.sleep(4)
        print("valid information on search page is work correct. TC - 008 IS PASSED")

        # Close entire Browser:
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(AllureReports)