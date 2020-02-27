import unittest
from TwoSum import Solution


class TwoSumTest(unittest.TestCase):
    def test_first_two(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 1
        self.assertEqual(temp.twoSum(self.list, self.target), [0, 1])

    def test_last_two(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 13
        self.assertEqual(temp.twoSum(self.list, self.target), [6, 7])

    def test_long_list(self):
        temp = Solution()
        self.list = list(range(10001))
        self.target = 19999
        self.assertEqual(temp.twoSum(self.list, self.target), [9999,10000])


if __name__ == "__main__":
    unittest.main()
