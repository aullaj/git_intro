import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        input = ""
        expected = False
        self.assertEqual(input, expected)


if __name__ == '__main__':
    unittest.main()
