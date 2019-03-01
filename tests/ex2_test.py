import unittest
from ex2 import ex2_1
from ex2 import ex2_2

class TestOutputEx2(unittest.TestCase):

    def test__checksum(self):
        self.assertEqual(ex2_1.checksum("ex2/inputs/inputDavid1.txt"), 6696)
        self.assertEqual(ex2_1.checksum("ex2/inputs/inputDavid2.txt"), 12)

    def test__findTwice(self):
        self.assertEqual(ex2_2.findTwice("ex2/inputs/inputDavid1.txt"), 'bvnfawcnyoeyudzrpgslimtkj' )
        self.assertEqual(ex2_2.findTwice("ex2/inputs/inputDavid2.txt"), 'abcde')
        self.assertEqual(ex2_2.findTwice("ex2/inputs/inputDavid3.txt"), 'bcde')


if __name__ == '__main__':
    unittest.main()
