import unittest

def suma(a, b):
    """Suma dos números enteros."""
    return a + b    

# Creamos la clase TestSuma
class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(4, 9), 13)  # 4 + 9 = 13

    def test_suma_negativos(self):
        self.assertEqual(suma(-4, -9), -13)  # -4 + (-9) = -13

# Punto de entrada para ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
