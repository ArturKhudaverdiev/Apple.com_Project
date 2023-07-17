#Verify that user without authorized account can send text to apple support

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import helpers as hp
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#Open chrome browser
driver = webdriver.Chrome()

#Open Apple website home page
driver.get(hp.url)
driver.maximize_window()
time.sleep(2)

#Check that we are on the right website

assert "Apple" in driver.title
print("Apple Page Title is: ", driver.title)
time.sleep(2)

#Go to in Account on Bag submenu
driver.find_element(By.XPATH, "//a[@id='globalnav-menubutton-link-bag']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ac-gn-bagview-nav-text'][contains(.,'Account')]").click()
time.sleep(1.5)

#Click to chat now link-text
driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Chat now (Opens in a new window)')]").click()
time.sleep(8)

all_windows = driver.window_handles

popup_window = all_windows[-1]
driver.switch_to.window(popup_window)

driver.find_element(By.XPATH, "//html")
driver.set_window_size(1000, 900)
time.sleep(4)

assert "We’re here to help.", driver.findElement(By.XPATH, "//h1[contains(.,'We’re here to help.')]").getText()
print("The H1 if new window is correct", driver.title)
driver.find_element(By.XPATH, "//button[contains(.,'Connect With A Specialist')]").click()
time.sleep(5)

#Click to "Chat with us Online" button
driver.find_element(By.XPATH, "//h2[contains(.,'Chat with us online.')]").click()
time.sleep(5)

#In input field send message enter "Hi"
driver.find_element(By.XPATH, "//textarea[contains(@id,'userMessage')]").send_keys("Hi")
time.sleep(4)
driver.find_element(By.XPATH, "//button[@id='sendIcon']").click()
time.sleep(4)

#Close window
driver.close()












