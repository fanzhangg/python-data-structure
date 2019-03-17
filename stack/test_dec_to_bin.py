from unittest import TestCase

from number_converter import dec_to_bin


class TestDecToBin(TestCase):
    def test_dec_to_bin(self):
        num = 233
        bin_str = dec_to_bin(num)
        self.assertEqual("11101001", bin_str)
