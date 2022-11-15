import unittest
from selenium import webdriver
import time
import allure


@allure.feature(u'Test Prueba 1')
@allure.story(u'015: Visitar GainInterview y calcular numero')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio GainInterView:</br>'
Deseamos ingresar un numero en el textbox</br></br></br>""")
class test_004(unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a GainInterView'):
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()
            self.driver.get('https://qainterview.pythonanywhere.com/')

    def test_004(self):
        with allure.step(u'PASO 2: Ingresar a el numero'):
            self.driver.find_element('id', 'number').send_keys('25')
            time.sleep(2)
            self.driver.find_element('id', 'number').clear()
            time.sleep(2)
            self.driver.find_element('id', 'number').send_keys('50')
            time.sleep(2)
            self.driver.find_element('id', 'getFactorial').click()

    def tearDown(self):
        with allure.step(u'PASO 3: Cerrar el navegador'):
            time.sleep(15)
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
