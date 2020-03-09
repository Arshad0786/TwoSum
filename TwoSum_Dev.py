class Solution:
    def twoSum(self, nums=[], target=None):
        output = list()

        def notInt(input):
            if type(input) != type(int()):
                return True
            else:
                return False

        for number in nums:
            if (notInt(number) or notInt(target)):
                return None

        try:
            for number in nums:
                if((target - number) not in nums):
                    continue

                if((target - number == number) and nums.count(number) == 1):
                    continue

                output = ([nums.index(number), nums.index(
                    target - number, nums.index(number)+1)])

                return output

            else:
                return None

        except SyntaxError:
            return None
