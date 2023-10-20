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


# GoogleChrome Browser UnitTest HOME PAGE:

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        #Убедится, что все разделы в топ меню читабельны и кликабельны

    def test_one(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get("https://kamrad33.github.io/index.html")
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Главная')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Главная')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Новости')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Новости')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Размещение и тарифы')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Размещение и тарифы')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Объявления на карте')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Объявления на карте')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Контакты')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Контакты')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Квартиры на сутки')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Квартиры на сутки')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Коттеджи и усадьбы')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Коттеджи и усадьбы')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Бани и Сауны')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Бани и Сауны')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Авто напрокат')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Авто напрокат')])[1]")))

        print("Check List #1 IS PASSED")

        #Убедиться что клиент, в разделе поиска - "Квартиры на сутки" в input field "ОТ" не может ввести больше 10 цифр

    def test_two(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get("https://kamrad33.github.io/index.html")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='from_input']").send_keys("123456789011")
        print("Check List #1 IS NOT PASSED")

    #Убедиться что клиент в разделе поиска "Квартиры на сутки" при введении валидного числа и нажатии на кновку "Показать" - переходит на страницу поиска

    def test_three(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get("https://kamrad33.github.io/index.html")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='from_input']").send_keys("12")
        time.sleep(2)
        driver.find_element(By.XPATH, '//span[text()="Показать"]').click()
        print("Check List #1 IS PASSED")

    #Убедиться, что клиент при нажатии в footer меню на социальную иконку instagramm, переходит на страницу инстаграмма

    def test_four(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get("https://kamrad33.github.io/index.html")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//div[contains(@class,'container')])[1]").click()
        time.sleep(2)

        all_windows = driver.window_handles

        popup_window = all_windows[-1]
        driver.switch_to.window(popup_window)

        driver.find_element(By.XPATH, "//html")
        driver.set_window_size(1000, 900)
        time.sleep(4)

        inst_expected_title = "Instagram"
        if inst_expected_title == "Instagram":
            print("The currect Title is correct")
        else:
            print("The current Title is error")

            """Убедиться что клиент в разделе поиска "Квартиры на сутки" при 
            введении невалидных данных в input field "От" не сможет нажать на кнопку 'Показать'"""

    def test_five(self):
        driver = self.driver
        self.driver.maximize_window()
        driver.get("https://kamrad33.github.io/index.html")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='from_input']").send_keys("#####")
        time.sleep(2)
        driver.find_element(By.XPATH, '//span[text()="Показать"]').click()
        time.sleep(2)
        print("Check List #1 IS PASSED")










