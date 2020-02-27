class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            tempList = nums.copy()
            # Create a list that doesn't include current element (index = i)
            tempList.pop(i)
            for j in range(len(tempList)):
                # print([tempList[j],target,nums[i]])
                if (tempList[j] == target - nums[i]):
                    ls = [i, nums.index(tempList[j])]
                    return ls
        else:
            return None


"""
explain : if A + B = target, then A = target - B,
so if we have a list [3,7,12,4],
we scan through the elements one by one to check if the rest of elements in the list
equals target - current element.
Ex:set target to 15, we choose 3 -> we create a list of [7,12,4], then we scan if 7, 12, 4 = 15 - 3
12 does, then we output the index of both 3 and 12.
"""
