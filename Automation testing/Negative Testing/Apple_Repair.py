from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

     #1. Verify that user cannot enter invalid email in "Apple Support will call you" page

    def test_with_invalid_email(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Zack")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    # 2. Verify that user cannot enter invalid first name in "Apple Support will call you" page

    def test_with_invalid_first_name(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Z---___///")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    # 3. Verify that user cannot enter invalid last name in "Apple Support will call you" page
    def test_with_invalid_first_name(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Z---___///")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

     #1. Verify that user cannot enter invalid email in "Apple Support will call you" page

    def test_with_invalid_email(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Zack")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    # 2. Verify that user cannot enter invalid first name in "Apple Support will call you" page

    def test_with_invalid_first_name(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Z---___///")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    # 1. Verify that user cannot enter invalid last name in "Apple Support will call you" page
    def test_with_invalid_last_name(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Z---___///")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")


class EdgeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

     #1. Verify that user cannot enter invalid email in "Apple Support will call you" page

    def test_with_invalid_email(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Zack")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    # 2. Verify that user cannot enter invalid first name in "Apple Support will call you" page

    def test_with_invalid_first_name(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Z---___///")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    # 1. Verify that user cannot enter invalid last name in "Apple Support will call you" page
    def test_with_invalid_last_name(self):
        driver = self.driver
        #Open website Apple.com (Home page)
        driver.get("https://www.apple.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)


        #In top menu navigate to "Support"
        top_menu_support = driver.find_element(By.XPATH, "(//span[contains(.,'Support')])[1]")
        top_submenu_repair = driver.find_element(By.XPATH, "//a[contains(.,'Repair')]")
        actions = ActionChains(driver)
        actions.move_to_element(top_menu_support).perform()
        time.sleep(2)

        #In submenu click to "Repair"
        actions.move_to_element(top_submenu_repair).click().perform()
        time.sleep(5)

        #Click to "Start a repair" button
        driver.find_element(By.XPATH, "//span[contains(.,'Start a repair')]").click()
        time.sleep(3)

        """#In "More Devices and Services" Click to "Show all" button
        driver.find_element(By.XPATH, "(//span[contains(.,'Show')])[1]")
        time.sleep(3)"""

        #Click to Iphone cart
        driver.find_element(By.XPATH, "(//span[contains(.,'iPhone')])[3]").click()
        time.sleep(3)

        #Click to "Password and Security"
        driver.find_element(By.XPATH, "(//span[contains(.,'Passwords & Security')])[2]").click()
        time.sleep(3)

        #In "Choose a topic" click to "Apple ID disabled"
        driver.find_element(By.XPATH, "(//span[contains(.,'Apple ID disabled')])[3]").click()
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        time.sleep(2)

        #In "Contact" click to "Call" cart
        driver.find_element(By.XPATH, "//label[contains(@for,'CALL')]").click()
        time.sleep(2)

        #In input field "Phone number" enter valid phone number
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7079564231")
        time.sleep(2)

        #In input field "First Name" enter any valid first name
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Z---___///")
        time.sleep(2)

        #In input field "Last Name" enter any valid last name
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Zacker")
        time.sleep(2)

        #In input field "Email" enter any invalid email
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("%%%@gmail.com")
        time.sleep(2)

        #Click to "Continue" button
        driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        time.sleep(2)

        #Confirm that information was sent
        h1 = driver.find_element(By.XPATH, "//*[text()='You’ll get a call.']")

        # Check if the element contains the text "Welcome"
        h1_text = "You’ll get a call."
        if h1_text in h1.text:
            print(f"The element contains the {h1_text}.")
        else:
            print(f"The element does not contain the search text: {h1_text}.")

    def tearDown(self):
        self.driver.quit()






