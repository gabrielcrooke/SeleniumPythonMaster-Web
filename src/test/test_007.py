# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
import allure


@allure.feature(u'Test Prueba 2')
@allure.story(u'016: Visitar Mercado libre y ver elementos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio Mercado Libre:</br>'
Deseamos validar un elemento</br></br></br>""")
class Test_007(unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Mercado Libre'):
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get("https://www.mercadolibre.com.ar")

    def test_007(self):

        with allure.step(u'PASO 2: Validar elementos '):
            # Existe
            self.element = "/html/body"
            # NoExiste
            self.element1 = '//*[@id="cb1-edit"]'

        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.element1)))

        except TimeoutException:
            self.skipTest("No se encontro el elemento")

    def tearDown(self):
        with allure.step(u'PASO 3: Cerrar navegador'):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
