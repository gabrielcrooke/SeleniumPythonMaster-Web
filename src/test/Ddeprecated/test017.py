# Identificacon de la existencia de los elementos de la pagina

# -*- coding: utf-8 -*-
'''
Created on 04 oct. 2022
@author: Gabriel
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure

horaGlobal = time.strftime('%H%M%S')


@allure.feature(u'Test Prueba 3')
@allure.story(u'016: Visitar Google y accion')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio Google:</br>'
Deseamos realizar algunas acciones</br></br></br>""")
class Test_001(unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Google'):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(15)
            self.driver.get("https://www.google.com.do/")

    def test_001(self):
        # INGRESO A LA APP DE REGISTRO

        with allure.step(u'PASO 2: Interactuar con elementos'):
            self.driver.find_element('xpath',
                                     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
                'Documentacion de python')
            self.driver.find_element('xpath',
                                     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
                Keys.BACK_SPACE, Keys.BACK_SPACE)
            self.driver.find_element('xpath',
                                     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
                Keys.ENTER)

            self.driver.get_screenshot_as_file(
                f"C:/udemy.python.SeleniumFramework/src/data/capturasPrueba/{horaGlobal}.png")
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def tearDown(self):
        with allure.step(u'PASO 3: Cerrar el navegador'):
            time.sleep(20)
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
