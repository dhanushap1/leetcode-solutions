
"""
LeetCode 11 - Container With Most Water

Problem:
Given an integer array height, where each element
represents the height of a vertical line, find two
lines that form a container holding the maximum amount
of water.

The container cannot be slanted.

Approach: Two Pointers

1. Initialize left at the beginning.
2. Initialize right at the end.
3. Calculate the area using:
   min(height[left], height[right]) * (right - left)
4. Update the maximum area.
5. Move the pointer pointing to the shorter line.
6. Repeat until both pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/container-with-most-water/
"""

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)

            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
