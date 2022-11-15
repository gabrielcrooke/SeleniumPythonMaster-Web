# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from src.pages.Spotify_registro import Registro


class Test_012(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.spotify.com/do/signup')

    def test_012(self):
        self.driver.find_element('xpath', Registro.img_logo_xpath)

        assert self.driver.find_element('xpath', Registro.label_titulo_xpath).text == 'Regístrate gratis para escuchar.'
        print(self.driver.find_element('xpath', Registro.label_titulo_xpath).text)

        self.driver.find_element('xpath', Registro.txt_correo_xpath).send_keys('gabrielcrooke@gmail.com')
        self.driver.find_element('xpath', Registro.txt_ccorreo_xpath).send_keys('gabrielcrookel@gmail.com')

        self.driver.find_element('xpath', Registro.txt_pass_xpath).send_keys('Prueba1234')

        self.driver.find_element('xpath', Registro.txt_apodo_xpath).send_keys('Gaby')

        smsEmail = self.driver.find_element('xpath', Registro.sms_alert_dcorreo).text

        if smsEmail:
            assert smsEmail == "Las direcciones de correo electrónico no coinckiden."
            print('Encontrado')

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
