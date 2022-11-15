import unittest

class Test001(unittest.TestCase):

    def setUp(self):
        self.variable_a = 50
        self.variable_b = 50

    def test_001(self):

        self.Resultado = self.variable_a + self.variable_b

    def tearDown(self):
        self.assertTrue(self.Resultado == 100, f"EL valor no es 10,es {self.Resultado}")


class Test002(unittest.TestCase):

    def setUp(self):
        self.variable_a = 'Gabriel '
        self.variable_b = 'Enrique'

    def test_002(self):

        self.Resultado = self.variable_a + self.variable_b

    def tearDown(self):
        self.assertEqual('Gabriel Enrique', self.Resultado, f"El resultado esperado no coincide,es: {self.Resultado}")

if __name__ == '__main__':
    unittest.main()
