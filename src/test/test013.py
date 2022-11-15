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
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from src.pages.Spotify_registro import Registro
import json

class Test_013(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.spotify.com/do/signup')


    def test_013(self):


    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
