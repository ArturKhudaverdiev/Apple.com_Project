#Verify that client can add 2 Mackbooks Air in Bag without account authorization

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

#go to website Apple.com
driver.get("https://www.apple.com/")
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(2)

#assert that we are the right website and the Title of Apple.com is correct
assert "Apple" in driver.title
print("The title of Apple is CORRECT:", driver.title)

#Go to "Shop Mac" page
time.sleep(2)
top_menu_mac = driver.find_element(By.XPATH, "(//span[contains(.,'Mac')])[1]")
top_submenu_shop_mac = driver.find_element(By.XPATH, "//a[contains(.,'Shop Mac')]")
actions = ActionChains(driver)
actions.move_to_element(top_menu_mac).perform()
time.sleep(2)
actions.move_to_element(top_submenu_shop_mac).click().perform()
time.sleep(2)

#In Carousel select "MacBook Air 13” and 15” with M2 chip" Card and click "Buy button"
driver.find_element(By.XPATH, "//a[@href='/shop/buy-mac/macbook-air/15-inch-m2']").click()
time.sleep(1.5)

#Select "15-inch (M2 chip)From $1299" and "Starlight" color
driver.find_element(By.XPATH, "//span[contains(.,'15-inch (M2 chip)')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//img[@width='32'])[17]").click()
time.sleep(2)

#click "Select" button
driver.find_element(By.XPATH, "//button[@data-autom='proceed-15inch-best']").click()
time.sleep(1.5)

#click to "Add to Bag" button
driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
time.sleep(1.5)

#click "Review to Bag" button
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(1.5)

#Click to drop down "Show product details" text
driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[3]").click()
time.sleep(1.5)

driver.close()















