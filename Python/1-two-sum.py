"""
LeetCode 1 - Two Sum

Problem:
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add
up to the target.

You may assume that each input has exactly one solution,
and you cannot use the same element twice.

Examples:

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Approach:
Use a hash map to store numbers and their indices.
For each number, calculate its complement.
If the complement exists in the hash map, return
the indices. Otherwise, store the current number.

Time Complexity: O(n)
Space Complexity: O(n)

LeetCode:
https://leetcode.com/problems/two-sum/
"""
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
