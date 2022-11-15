# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
from selenium import webdriver

from pages.Spotify_registro import Registro as Spoty_registro


class Test_008(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        # INGRESO A LA APP DE REGISTRO
        self.driver.get("https://www.spotify.com/do/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")

    def test_008(self):

        self.driver.find_element('xpath', Spoty_registro.txtCorreo).send_keys('josefeliciano@gmail.com')
        self.driver.find_element('xpath', Spoty_registro.txtCcorreo).send_keys('josefeliciano@gmail.com')
        self.driver.find_element('xpath', Spoty_registro.txtPass).send_keys('Pene0213')
        self.driver.find_element('xpath', Spoty_registro.txtApo).send_keys('La Parita')




if __name__ == "__main__":
    unittest.main()