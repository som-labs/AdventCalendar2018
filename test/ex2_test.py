import unittest
from ex2 import ex2_1


class TestOutputEx2(unittest.TestCase):

    def test__checksum(self):
        self.assertEqual(ex2_1.checksum("ex2/input/inputDavid1.txt"), 6696)
        self.assertEqual(ex2_1.checksum("ex2/input/inputDavid2.txt"), 12)


if __name__ == '__main__':
    unittest.main()
