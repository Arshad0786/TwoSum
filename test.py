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

    def test_negetive_in_list_and_target(self):
        temp = Solution()
        self.list = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
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

    def test_none_integer_target(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.target = ""
        self.assertEqual(temp.twoSum(self.list, self.target), None)

    def test_target_isnt_given(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(temp.twoSum(nums=self.list), None)

    def test_nums_isnt_given(self):
        temp = Solution()
        self.target = 20
        self.assertEqual(temp.twoSum(target=self.target), None)

    def test_two_same_num(self):
        temp = Solution()
        self.target = 40
        self.list = [0, 20, 39, 50, 7, 20]
        self.assertEqual(temp.twoSum(self.list, self.target), [1,5])

    def test_one_same_num(self):
        temp = Solution()
        self.target = 40
        self.list = [0, 20, 39, 50, 7]
        self.assertEqual(temp.twoSum(self.list, self.target), None)

    def both_one_and_two_same_num(self):
        temp = Solution()
        self.target = 6
        self.list = [3,2,4]
        self.assertEqual(temp.twoSum(self.list, self.target), [1,2])

if __name__ == "__main__":
    unittest.main()
