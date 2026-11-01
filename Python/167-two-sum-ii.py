
"""
LeetCode 167 - Two Sum II - Input Array Is Sorted

Problem:
Given a 1-indexed sorted array of integers numbers and
a target value, find two numbers whose sum equals target.

Return their 1-based indices as [index1, index2].

You cannot use the same element twice.
The solution must use O(1) extra space.

Example 1:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]

Example 2:
Input: numbers = [2, 3, 4], target = 6
Output: [1, 3]

Example 3:
Input: numbers = [-1, 0], target = -1
Output: [1, 2]

Approach: Two Pointers

1. Initialize left at the beginning of the array.
2. Initialize right at the end of the array.
3. Calculate the sum of both elements.
4. If the sum equals target, return their 1-based indices.
5. If the sum is smaller, move left forward.
6. If the sum is greater, move right backward.

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1
