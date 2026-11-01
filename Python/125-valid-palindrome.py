
"""
LeetCode 125 - Valid Palindrome

Problem:
Given a string s, convert uppercase letters to lowercase
and remove all non-alphanumeric characters.

Return True if the resulting string reads the same
forward and backward. Otherwise, return False.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: True
Explanation: An empty string is a palindrome.

Approach: String Manipulation
1. Convert the string to lowercase.
2. Keep only alphanumeric characters.
3. Reverse the cleaned string.
4. Compare the original cleaned string with its reverse.

Time Complexity: O(n)
Space Complexity: O(n)

LeetCode:
https://leetcode.com/problems/valid-palindrome/
"""

class Solution(object):
    def isPalindrome(self, s):
        t = ""

        l = s.lower()

        for c in l:
            if c.isalnum():
                t += c

        u = t[::-1]

        if u == t:
            return True
        return False

"""OR two pointer"""
class Solution(object):
    def isPalindrome(self, s):
        t = ""

        # Convert to lowercase and remove special characters
        s = s.lower()

        for c in s:
            if c.isalnum():
                t += c

        # Initialize two pointers
        left = 0
        right = len(t) - 1

        # Compare characters
        while left < right:
            if t[left] != t[right]:
                return False

            left += 1
            right -= 1

        return True
