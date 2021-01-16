import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_base11(self):
        self.assertEqual(convert(120, 11), 'AA')

    def test_base12(self):
        self.assertEqual(convert(143, 12), 'BB')

    def test_base14(self):
        self.assertEqual(convert(111, 14), '7D')

    def test_base15(self):
        self.assertEqual(convert(134, 15), '8E')

    def test_base16_second(self):
        self.assertEqual(convert(143, 16), '8F')

    def test_base16_third(self):
        self.assertEqual(convert(11259375,16),"ABCDEF")

    def test_base16_fourth(self):
        self.assertEqual(convert(27, 16), '1B')

    def test_base16_fifth(self):
        self.assertEqual(convert(28, 16), '1C')

    def test_base16_sixth(self):
        self.assertEqual(convert(29, 16), '1D')

    def test_base16_seventh(self):
        self.assertEqual(convert(30, 16), '1E')

    def test_base16_eigth(self):
        self.assertEqual(convert(31, 16), '1F')


if __name__ == "__main__":
        unittest.main()