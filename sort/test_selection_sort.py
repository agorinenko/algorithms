import unittest

from sort.selection_sort import SelectionSort


class DefaultTestCase(unittest.TestCase):
    def test_main(self):
        a = [31, 41, 59, 26, 41, 58]

        obj = SelectionSort()

        b = obj.sort(a)
        self.assertEqual(b[0], 26)
        self.assertEqual(b[1], 31)
        self.assertEqual(b[2], 41)
        self.assertEqual(b[3], 41)
        self.assertEqual(b[4], 58)
        self.assertEqual(b[5], 59)

    def test_main_1(self):
        a = [1, 2, 3, 4, 5, 6]

        obj = SelectionSort()

        b = obj.sort(a)
        self.assertEqual(b[0], 1)
        self.assertEqual(b[1], 2)
        self.assertEqual(b[2], 3)
        self.assertEqual(b[3], 4)
        self.assertEqual(b[4], 5)
        self.assertEqual(b[5], 6)

    def test_main_2(self):
        a = [6, 5, 4, 3, 2, 1]

        obj = SelectionSort()

        b = obj.sort(a)
        self.assertEqual(b[0], 1)
        self.assertEqual(b[1], 2)
        self.assertEqual(b[2], 3)
        self.assertEqual(b[3], 4)
        self.assertEqual(b[4], 5)
        self.assertEqual(b[5], 6)

    def test_main_3(self):
        a = [1, 2, 3, 4, 5, 6]

        obj = SelectionSort()

        b = obj.sort(a, reverse=True)
        self.assertEqual(b[0], 6)
        self.assertEqual(b[1], 5)
        self.assertEqual(b[2], 4)
        self.assertEqual(b[3], 3)
        self.assertEqual(b[4], 2)
        self.assertEqual(b[5], 1)
