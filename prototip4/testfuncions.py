import unittest
def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

class TestFuncions(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(9, 3), 6)  # 9 - 3 = 6
    
    def test_divideix_normal(self):
        self.assertEqual(divideix(50, 5), 10)  # 50 / 5 = 10
    
    def test_divideix_per_zero(self):
        self.assertEqual(divideix(5, 0), "Error: divisió per zero")

if __name__ == '__main__':
    unittest.main()