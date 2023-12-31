#Verify that user cannot buy 1000 MacBooksAir 15
#Verify that client can add 2 Mackbooks Air in Bag without account authorization

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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

#Go to "Explore Mac - MAcBook AIR" page
time.sleep(2)
top_menu_mac = driver.find_element(By.XPATH, "(//span[contains(.,'Mac')])[1]")
top_submenu_mac_air = driver.find_element(By.XPATH, "//a[@href='/macbook-air/'][contains(.,'MacBook Air')]")
actions = ActionChains(driver)
actions.move_to_element(top_menu_mac).perform()
time.sleep(2)
actions.move_to_element(top_submenu_mac_air).click().perform()
time.sleep(5)

#In Submenu click to laptop picture with title "MacBook AIR M2 chip. New 15" model"
driver.find_element(By.XPATH, "(//figure[@class='chapternav-icon'])[2]").click()
time.sleep(3)

#On the submenu click to "Buy" button
driver.find_element(By.XPATH, "//a[@class='ac-ln-button']").click()
time.sleep(3)

#In "8-Core CPU 10-Core GPU 8GB Unified Memory 512GB SSD Storagefootnote¹" specification choose any color and click "Select" button
driver.find_element(By.XPATH, "(//button[@type='submit'])[6]").click()
time.sleep(3)

#Click to "Add to Bag" button
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(3)

#Click to "Review to Bag"
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(3)

#Click to drop down menu quantity and choose 10+
driver.find_element(By.XPATH, "//select[@data-autom='item-quantity-dropdown']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//select[contains(@class,'rs-quantity-dropdown form-dropdown-select')]//option[@value ='10']").click()
time.sleep(3)

#Delete 10 qualtity
driver.find_element(By.XPATH, "//input[contains(@type,'tel')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[contains(@type,'tel')]").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element(By.XPATH, "//input[contains(@type,'tel')]").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element(By.XPATH, "//input[contains(@type,'tel')]").send_keys("1000")
time.sleep(2)

#Click to checkout button
driver.find_element(By.XPATH, "//button[@id='shoppingCart.actions.checkout']").click()
time.sleep(3)

driver.close()




