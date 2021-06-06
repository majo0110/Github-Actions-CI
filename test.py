import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(10, 15), 25)

    def test_subtraction(self):
        self.assertEqual(example.subtract(40, 15), 25)

    def test_multiply(self):
        self.assertEqual(example.multiply(15, 10), 150)


if __name__ == '__main__':
    unittest.main()
