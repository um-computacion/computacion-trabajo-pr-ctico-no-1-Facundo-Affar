import unittest
from src.conversion_romano import decimal_a_romano

class TestConversion(unittest.TestCase):

    def test_uno(self):
        self.assertEqual(decimal_a_romano(1), 'I')

    def test_cuatro(self):
        self.assertEqual(decimal_a_romano(4), 'IV')

    def test_cinco(self):
        self.assertEqual(decimal_a_romano(5), 'V')

    def test_nueve(self):
        self.assertEqual(decimal_a_romano(9), 'IX')

    def test_diez(self):
        self.assertEqual(decimal_a_romano(10), 'X')
    
    def test_valores_complejos(self):
        self.assertEqual(decimal_a_romano(49), 'XLIX')
        self.assertEqual(decimal_a_romano(3999), 'MMMCMXCIX')

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            decimal_a_romano(0)
        with self.assertRaises(ValueError):
            decimal_a_romano(4000)
        with self.assertRaises(ValueError):
            decimal_a_romano(-1)


if __name__ == '__main__':
    unittest.main()