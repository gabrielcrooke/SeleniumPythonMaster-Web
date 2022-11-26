import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from functions.Functions import funcionesGlobales


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        t = 2

    def test1(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.Navegar("https://qainterview.pythonanywhere.com/", 1)
        f.Texto_Mixto("id", "number", "10", 3)
        f.Texto_Mixto("xpath", "//input[contains(@id,'number')]", "15", 2)
        f.Click_Mixto("id", "getFactorial", 3)
        f.Click_Mixto("xpath", "//a[@href='/privacy']", 2)
        f.Salida()

    def test2(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.Navegar("https://www.onapi.gov.do/index.php/formulario-de-registro", 1)
        f.Select_Xpath_Type("//select[@id='limit']", "value", "0", 2)
        f.Salida()

    def test3(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", 1)
        f.Upload_xpath("//input[@id='uploadPicture']", "C://udemy.python.SeleniumFramework//src//data//capturas"
                                                       "//error.png", 2)
        f.Salida()

    def test4(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", 1)
        f.Check_Xpath("//label[@for='gender-radio-1']", 2)
        f.Check_Xpath("//label[@for='hobbies-checkbox-2']", 2)
        f.Salida()

    def test5(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", 1)
        for num in range(4, 7):
            f.Check_Xpath_Multiples(2, "(//label[contains(@class,'custom-control-label')])[" + str(num) + "]")
        f.Salida()

    def test6(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", 1)
        f.Texto_Mixto("xpath", "(//input[@type='text'])[1]", "Gabriel", 2)
        f.Texto_Mixto("id", "lastName", "Crooke", 2)
        f.Salida()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
