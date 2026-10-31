
"""
LeetCode 283 - Move Zeroes

Problem:
Given an integer array nums, move all zeroes to the
end while maintaining the relative order of non-zero
elements.

The operation must be performed in-place.

Example 1:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Example 2:
Input: nums = [0]
Output: [0]

Approach: Using an Extra List
1. Store all non-zero elements in a new list.
2. Append zeroes to the list.
3. Replace the original array contents.

Time Complexity: O(n)
Space Complexity: O(n)

Note:
This approach produces the correct output but does
not satisfy the in-place requirement.

LeetCode:
https://leetcode.com/problems/move-zeroes/
"""

class Solution(object):
    def moveZeroes(self, nums):
        m = []

        for n in range(len(nums)):
            if nums[n] != 0:
                m.append(nums[n])

        for n in range(len(nums)):
            if nums[n] == 0:
                m.append(0)
        """
        nums.clear()
        for i in m:
          nums.append(i)
    """
        nums[:] = m
