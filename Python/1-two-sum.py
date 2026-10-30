
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


# Example
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

======================================================================OR==================================================================
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
             for j in range(i,len(nums)):
                if(i!=j and nums[i]+nums[j]==target):
                    return [i,j] 
        return []
