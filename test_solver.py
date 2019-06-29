import unittest

from argparse import ArgumentTypeError
from solver import validate_center, validate_outer


class TestValidation(unittest.TestCase):

    def test_center_valid(self):
        self.assertEqual('o', validate_center('o'))

    def test_center_multiple(self):
        with self.assertRaises(ArgumentTypeError):
            validate_center('fo')

    def test_center_number(self):
        with self.assertRaises(ArgumentTypeError):
            validate_center('1')

    def test_center_symbol(self):
        with self.assertRaises(ArgumentTypeError):
            validate_center('%')

    def test_center_none(self):
        with self.assertRaises(ArgumentTypeError):
            validate_center(None)

    def test_outer_valid(self):
        self.assertEqual('qwerty', validate_outer('qwerty'))

    def test_outer_smaller(self):
        with self.assertRaises(ArgumentTypeError):
            validate_outer('qwert')

    def test_outer_larger(self):
        with self.assertRaises(ArgumentTypeError):
            validate_outer('qwertyu')

    def test_outer_number(self):
        with self.assertRaises(ArgumentTypeError):
            validate_outer('qwert1')

    def test_outer_symbol(self):
        with self.assertRaises(ArgumentTypeError):
            validate_outer('qwert!')

    def test_outer_none(self):
        with self.assertRaises(ArgumentTypeError):
            validate_outer(None)


if __name__ == '__main__':
    unittest.main()
