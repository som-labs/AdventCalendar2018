import unittest
from ex1 import ex1_1
from ex1 import ex1_2


class TestOutputEx1(unittest.TestCase):

    def test__frequencies(self):
        self.assertEqual(ex1_1.frequencies("ex1/input/inputDavid1.txt"), 569)
        self.assertEqual(ex1_1.frequencies("ex1/input/inputDavid2.txt"), 4)
        self.assertEqual(ex1_1.frequencies("ex1/input/inputDavid3.txt"), 4)
        self.assertEqual(ex1_1.frequencies("ex1/input/inputDavid4.txt"), 1)

    def test__frequencies2(self):
        self.assertEqual(ex1_2.frequencies2("ex1/input/inputDavid1.txt"), 77666)
        self.assertEqual(ex1_2.frequencies2("ex1/input/inputDavid2.txt"), 10)
        self.assertEqual(ex1_2.frequencies2("ex1/input/inputDavid3.txt"), 5)
        self.assertEqual(ex1_2.frequencies2("ex1/input/inputDavid4.txt"), 14)


if __name__ == '__main__':
    unittest.main()
