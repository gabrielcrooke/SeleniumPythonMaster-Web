import unittest
from src.functions.Functions import Functions as Selenium

class Test_010(Selenium, unittest.TestCase):

    def setUp(self):

    Selenium.abrir_navegador()



    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()