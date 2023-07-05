#Verify that user can enter email in Vision Pro page

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import faker

driver = webdriver.Chrome()

#go to Apple website
driver.get("https://www.apple.com")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
time.sleep(1.5)

#open "Vision Pro" page
driver.find_element(By.XPATH, "(//span[contains(.,'Vision')])[1]").click()
time.sleep(1.5)

#click to "Notify Me" button
driver.find_element(By.XPATH, "(//button[contains(.,'Notify me')])[1]").click()
time.sleep(1.5)

#in input field click and enter valid email
driver.find_element(By.XPATH, "//input[contains(@type,'email')]").send_keys("talent@gmail.com")
time.sleep(1.5)

driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(4)

#Confirm that the "Stay up to date" pop up is open
assert "Stay up to date.", driver.findElement(By.XPATH, "Stay up to date.").getText()
print("The pop up test notify is correct")

driver.close()


