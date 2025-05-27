import unittest
from converter import convert_currency


class TestCurrencyConverter(unittest.TestCase):
    def test_usd_to_eur(self):
        self.assertAlmostEqual(convert_currency(100, 'USD', 'EUR'), 85.0, delta=0.1)

    def test_eur_to_rub(self):
        self.assertAlmostEqual(convert_currency(100, 'EUR', 'RUB'), 8823.53, delta=1.0)

    def test_rub_to_usd(self):
        self.assertAlmostEqual(convert_currency(7500, 'RUB', 'USD'), 100.0, delta=0.1)

    def test_invalid_currency(self):
        with self.assertRaises(KeyError):
            convert_currency(100, 'USD', 'JPY')

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            convert_currency(-100, 'USD', 'EUR')

    def test_zero_amount(self):
        self.assertEqual(convert_currency(0, 'USD', 'EUR'), 0.0)

    def test_non_numeric_amount(self):
        with self.assertRaises(TypeError):
            convert_currency("100", 'USD', 'EUR')


if __name__ == '__main__':
    unittest.main()
