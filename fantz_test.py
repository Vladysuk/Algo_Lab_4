import unittest
from dynamic_approach import count_min_slices, count_number_powers


class MyTestCase(unittest.TestCase):
    def test_from_task(self):
        self.assertEqual(count_min_slices("101101101", 5), 3)
        self.assertEqual(count_min_slices("1111101", 5), 1)
        self.assertEqual(count_min_slices("110011011", 5), 3)
        self.assertEqual(count_min_slices("10011101111010010011111011001110010100011110010111001000110011101111"
                                          "0100100111110110011100101000110010110000111100101110010001", 7), 5)

        self.assertEqual(count_min_slices('101111101', 5), 5)

        self.assertEqual(count_min_slices('111110100', 2), 6)
        self.assertEqual(count_min_slices('10101', 5), -1)
        self.assertEqual(count_min_slices('10110011', 5), -1)
