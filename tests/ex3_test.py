import unittest
from ex3 import ex3_1
from ex3 import ex3_2


class TestOutputEx3(unittest.TestCase):

    def test__checksum(self):
        path = "ex3/inputs/inputMarta"
        self.assertEqual(ex3_1.get_boxes_overlaped(path + "1.txt"), 104241)
        self.assertEqual(ex3_1.get_boxes_overlaped(path + "2.txt"), 4)

    def test__findTwice(self):
        path = "ex3/inputs/inputMarta"
        self.assertEqual(ex3_2.get_box(path + "1.txt"), "806")
        self.assertEqual(ex3_2.get_box(path + "2.txt"), "3")


if __name__ == '__main__':
    unittest.main()
