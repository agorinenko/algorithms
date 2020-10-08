import unittest

from sort.insertion_sort import InsertionSort


class DefaultTestCase(unittest.TestCase):
    def test_main(self):
        a = [31, 41, 59, 26, 41, 58]

        obj = InsertionSort()

        b = obj.sort(a)
        self.assertEqual(b[0], 26)
        self.assertEqual(b[1], 31)
        self.assertEqual(b[2], 41)
        self.assertEqual(b[3], 41)
        self.assertEqual(b[4], 58)
        self.assertEqual(b[5], 59)
