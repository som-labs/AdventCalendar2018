
import unittest
from ex2 import ex2_1
from ex2 import ex2_2

path = "ex2/inputs/inputMarta"


class TestStringMethods(unittest.TestCase):
    def tests_ex2_1(self):
        self.assertEqual(ex2_1.checksum(path + "1.txt"), 7872)
        self.assertEqual(ex2_1.checksum(path + "2.txt"), 12)

    def tests_ex2_2(self):
        self.assertEqual(ex2_2.common_letters(path + "3.txt"), "tjxmoewpdkyaihvrndfluwbzc")
        self.assertEqual(ex2_2.common_letters(path + "4.txt"), "fgij")


if __name__ == '__main__':
    unittest.main()
