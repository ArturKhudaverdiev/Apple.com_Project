#Verify that all image on "Iphone 14 pro is visible"

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import helpers as hp

driver = webdriver.Chrome()

#go to website Apple.com
driver.get("https://www.apple.com/")
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(2)

#Go to  "Iphone 14 Pro" page
#In TOP MENU click on "Iphone"
driver.find_element(By.XPATH, "//span[@class='globalnav-link-text-container'][contains(.,'iPhone')]").click()
time.sleep(2)
#In subtop menu click to
driver.find_element(By.XPATH, "(//figure[contains(@class,'chapternav-icon')])[1]").click()
time.sleep(2)

#The main images on page
#Deep purple
elem_purple = driver.find_element(By.XPATH, "//img[@src='/v/iphone-14-pro/h/images/key-features/hero/hero_deep_purple__dlhl8s8j6wk2_large.jpg']")
if 'deep_purple' in elem_purple.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image DEEP PURPLE is visible on screen')
time.sleep(4)

#Gold
#Click to radiobuttom "Gold"
driver.find_element(By.XPATH, "//span[@class='colornav-swatch colornav-swatch-gold no-inversion'][contains(.,'Gold')]").click()
time.sleep(2)
elem_gold = driver.find_element(By.XPATH, '//li[@id="hero-gallery-item-gold"]')
if 'gold' in elem_gold.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image GOLD is visible on screen')
time.sleep(2)

#Silver
#Click to radiobuttom "Silver"
driver.find_element(By.XPATH, "//span[@class='colornav-swatch colornav-swatch-silver no-inversion'][contains(.,'Silver')]").click()
time.sleep(2)
elem_silver = driver.find_element(By.XPATH, '//li[@id="hero-gallery-item-silver"]')
if 'silver' in elem_silver.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image SILVER is visible on screen')
time.sleep(2)

#Space Black
#Click to radiobuttom "Silver"
driver.find_element(By.XPATH, "(//span[contains(.,'Space Black')])[1]").click()
time.sleep(2)
elem_space_black = driver.find_element(By.XPATH, '//li[@id="hero-gallery-item-space-black"]')
if 'space black' in elem_space_black.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image SPACE BLACK is visible on screen')
time.sleep(2)

#Meet Dynamic Island image
elem_dynamic_island = driver.find_element(By.XPATH, '//img[@alt="A stack of three Gold iPhone 14 Pro models showcasing the three different states of Dynamic Island."]')
if 'Dynamic Island' in elem_dynamic_island.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Dynamic Island image is visible on screen')
time.sleep(2)

# 48MP Main camera. Mind-blowing detail.
elem_main_camera = driver.find_element(By.XPATH, "//img[@src='/v/iphone-14-pro/h/images/key-features/features/main-camera/camera_gold__bjzgrypwq8wi_large.jpg']//..//img[@alt='A beautifully detailed photo taken in low light.']")
if 'detailed photo' in elem_main_camera.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image 48MP Main camera is visible on screen')
time.sleep(2)

#The mastermind behind it all image A16
elem_bionic_chip = driver.find_element(By.XPATH, '//div[text()="Illustrative representation of the A16 Bionic chip."]')
if 'A16 Bionic chip' in elem_bionic_chip.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image A16 Bionic chip image is visible on screen')
time.sleep(2)

#Ceramic Shield Tougher than any smartphone glass.
elem_ceramic_shield = driver.find_element(By.XPATH, "(//img[@alt='Side view of iPhone 14 Pro showcasing the Ceramic Shield front.'])[1]")
if 'ceramic-shield' in elem_ceramic_shield.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Ceramic Shield is visible on screen')
time.sleep(2)

#Water Resistance
elem_water_resistance = driver.find_element(By.XPATH, "(//div[@class='grid-tile-content'])[9]")
if 'grid-tile-content' in elem_water_resistance.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Water Resistance is visible on screen')
time.sleep(2)

#Emergency SOS
elem_emergency_sos = driver.find_element(By.XPATH, "//div[@class='overlay headline-content'][contains(.,'Emergency SOS via satellite')]")
if 'Emergency SOS' in elem_emergency_sos.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Emergency SOS is visible on screen')
time.sleep(2)

#A camera in a class by itselfie.
elem_it_selfie = driver.find_element(By.XPATH, "//img[@src='/v/iphone-14-pro/h/images/key-features/features/true-depth/selfie_deep_purple__fmaespigvcqe_large.jpg']")
if 'selfie_deep_purple' in elem_it_selfie.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image It selfie is visible on screen')
time.sleep(2)

#Crash Detection
elem_crash_detection = driver.find_element(By.XPATH, '//span[@class="visuallyhidden" and text()="Crash Detection"]')
if 'Crash Detection' in elem_crash_detection.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Crash Detection is visible on screen')
time.sleep(2)

#Pro Max Size image
elem_pro_max_size = driver.find_element(By.XPATH, "//img[@src='/v/iphone-14-pro/h/images/key-features/features/sizes/size_promax_deep_purple__ct7arcvi3vyq_large.jpg']")
if 'size_promax_deep_purple' in elem_pro_max_size.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Pro Max Size image is visible on screen')
time.sleep(2)

#Ways to save on iPhone.
#Get $200–$640 in credit toward iPhone 14 Pro when you trade in iPhone 11 or higher.1

elem_trade_in = driver.find_element(By.XPATH, '//div[@class="tile-image image-trade-in"]')
if 'image-trade-in' in elem_trade_in.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Image Get $200–$640 in credit toward iPhone 14 Pro is visible on screen')
time.sleep(2)

#Pay 0% APR over 24 months with Apple Card.†
elem_apple_card = driver.find_element(By.XPATH, '//div[@class="tile-image image-apple-card"]')
if 'image-apple-card' in elem_apple_card.get_attribute('class'):
    print ('Image is not visible on screen')
else:
    print ('Pay 0% APR over 24 months is visible on screen')
time.sleep(2)

driver.close()









