

import unittest

from ex1 import ex1_1
from ex1 import ex1_2


class TestStringMethods(unittest.TestCase):
    def test_cadena1(self):
        self.assertEqual(ex1_1.ex1_1("ex1/inputs/inputMarta1.txt"), 599)

    def test_cadena2(self):
        self.assertEqual(ex1_2.ex1_2("ex1/inputs/inputMarta3.txt"), 2)
        self.assertEqual(ex1_2.ex1_2("ex1/inputs/inputMarta2.txt"), 81204)
        self.assertEqual(ex1_2.ex1_2("ex1/inputs/inputMarta4.txt"), 10)


if __name__ == '__main__':
    unittest.main()
