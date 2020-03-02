class Solution:
    def twoSum(self, nums, target):
        TempNums = nums.copy()
        for i in nums:
            if(((target - i) in TempNums) and (i in TempNums) and (i != target - i)):
            #(i != target - i) : if target - i = i, ((target - i) in TempNums) and (i in TempNums) will be 
            #both True, but there will only be one value in TempNums, for example, let's have a list of 
            #[1,3,5,7,9] if the target is 10, then when 5 is being scanned, 5 and 10 - 5 are both in list,
            #but there is only one 5 in the List so it's invalid.
                output = ([nums.index(i), nums.index(target - i)])
                return output
        else:
            return None
                
        
