import unittest
from TwoSum_Dev import Solution


class TwoSumTest(unittest.TestCase):
    def test_last_two(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 13
        self.assertEqual(temp.twoSum(self.list, self.target), [6, 7])

    def test_target_no_match(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 100
        self.assertEqual(temp.twoSum(self.list, self.target), None)

    def test_long_list(self):
        temp = Solution()
        self.list = list(range(20001))
        self.target = 39999
        self.assertEqual(temp.twoSum(self.list, self.target), [19999, 20000])

    def test_first_last(self):
        temp = Solution()
        self.list = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        self.target = 21
        self.assertEqual(temp.twoSum(self.list, self.target), [0, 11])

    def test_possible_multiple_result(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = 7
        self.assertEqual(temp.twoSum(self.list, self.target), [0, 7])
        # Two Sum should output the first pair of numbers in the list that fits

    def test_negetive_in_list(self):
        temp = Solution()
        self.list = [0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        self.target = -11
        self.assertEqual(temp.twoSum(self.list, self.target), [1, 10])

    def test_empty_list(self):
        temp = Solution()
        self.list = []
        self.target = 100
        self.assertEqual(temp.twoSum(self.list, self.target), None)

    def test_none_integer_in_list(self):
        temp = Solution()
        self.list = [0.02, 1, 3, 5, 7, 9, 11, 13, 15, 0.98]
        self.target = 4
        self.assertEqual(temp.twoSum(self.list, self.target), None)


if __name__ == "__main__":
    unittest.main()
