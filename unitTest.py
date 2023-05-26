import unittest
from addnum import sum


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        result = sum(50, 50)
        self.assertEqual(result, 100)

    def test_sum_newnum(self):
        result = sum(5, 9)
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()
