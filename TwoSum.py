class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            if ((nums[i]+nums[i+1]) == target - nums[i]):
                ls = [i,i+1]
                return ls
            
            
            
        
output = Solution()
aList = [1,3,8,9]

print(output.twoSum(aList,17))