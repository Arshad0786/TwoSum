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
        self.assertEqual(temp.twoSum(self.list, self.target), [9999, 10000])
    
    def test_first_last(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 8
        self.assertEqual(temp.twoSum(self.list, self.target), [1, 7])

    def test_first_middle(self):
        temp = Solution()
        self.list = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        self.target = 13
        self.assertEqual(temp.twoSum(self.list, self.target), [0, 7])

    def test_middle_last(self):
        temp = Solution()
        self.list = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        self.target = 34
        self.assertEqual(temp.twoSum(self.list, self.target), [7, 11])

    def test_possible_multiple_result(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 7
        self.assertEqual(temp.twoSum(self.list, self.target), [0, 7])
        #Two Sum should output the first pair of numbers in the list that fits


if __name__ == "__main__":
    unittest.main()
