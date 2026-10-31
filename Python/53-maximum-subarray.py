
"""
LeetCode 53 - Maximum Subarray

Problem:
Given an integer array nums, find the contiguous
subarray with the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Approach: Brute Force
Use nested loops to generate every possible subarray.
Calculate its sum and update max_sum whenever a
larger sum is found.

Time Complexity: O(n^2)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/maximum-subarray/
"""

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]

        for n in range(len(nums)):
            current_sum = 0

            for m in range(n, len(nums)):
                current_sum += nums[m]

                if current_sum > max_sum:
                    max_sum = current_sum

        return max_sum
