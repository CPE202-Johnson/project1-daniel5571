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
        self.assertEqual(convert(120, 11), '10A')

    def test_base12(self):
        self.assertEqual(convert(143, 12), '11B')

    def test_base14(self):
        self.assertEqual(convert(111, 14), '7D')

    def test_base15(self):
        self.assertEqual(convert(134, 15), '8E')

    def test_base16_second(self):
        self.assertEqual(convert(143, 16), '8F')

if __name__ == "__main__":
        unittest.main()