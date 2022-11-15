# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
import src.pages.Spotify_registro


class Test_013(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.spotify.com/do/signup')

    def test_013(self):
        self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.img_logo_xpath)

        assert self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.label_titulo_xpath).text == 'Regístrate gratis para escuchar.'
        print(self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.label_titulo_xpath).text)

        self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.txt_correo_xpath).send_keys('gabrielcrooke@gmail.com')
        self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.txt_ccorreo_xpath).send_keys('gabrielcrooke@gmail.com')
        self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.txt_pass_xpath).send_keys('Prueba1234')

        self.driver.find_element('xpath', src.pages.Spotify_registro.Registro.txt_apodo_xpath).send_keys('Gaby')

        # SKIP
        self.driver.execute_script('window.scroll(0,600)', "")

        element = self.driver.find_element('xpath', '//*[@class="Button-qlcn5g-0 iuyipX"]')

        if element:
            element.is_displayed()
            unittest.TestCase.skipTest(self, 'Boton visible, no se ejecuto la prueba')

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
