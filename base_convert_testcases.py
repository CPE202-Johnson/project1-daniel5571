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
        self.assertEqual(convert(12, 16), 'C')

    def test_base16_fifth(self):
        self.assertEqual(convert(13, 16), 'D')

    def test_base16_sixth(self):
        self.assertEqual(convert(14, 16), 'E')

    def test_base16_seventh(self):
        self.assertEqual(convert(15, 16), 'F')


if __name__ == "__main__":
        unittest.main()