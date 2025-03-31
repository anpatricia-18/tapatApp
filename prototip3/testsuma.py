import unittest

def suma(a, b):
    """Suma dos números enteros."""
    return a + b    

##creem la clase TestSuma(unittest.TestCase):

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(4, 9), 13) # 9 + 4 = 13

        def test_suma_negativos(self):
            self.assertEqual(suma(-4, -9), -13) # -4 + (-9) = -13

    if __name__ == '__main__':
        unittest.main()

