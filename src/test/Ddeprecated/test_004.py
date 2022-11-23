import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


class test_004(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def test_004(self):
        self.driver.get('https://www.correoargentino.com.ar/')

        Select(self.driver.find_element('xpath',
                                        '//*[@id="block-block-15"]/div/div/div/div[2]/select')).select_by_visible_text(
            'DNI')

    def tearDown(self):
        time.sleep(15)

    if __name__ == '__main__':
        unittest.main()
