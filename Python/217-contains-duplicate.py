
"""
LeetCode 217 - Contains Duplicate

Problem:
Given an integer array nums, return True if any
element appears at least twice. Otherwise, return False.

Examples:
Input: nums = [1, 2, 3, 1]
Output: True

Input: nums = [1, 2, 3, 4]
Output: False

Approach:
Use a set to keep track of previously visited elements.
If an element is already in the set, return True.
Otherwise, add it to the set.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False
