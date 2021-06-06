import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(10, 15), 25)


if __name__ == '__main__':
    unittest.main()
