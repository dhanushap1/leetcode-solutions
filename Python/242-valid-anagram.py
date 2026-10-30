"""
LeetCode 242 - Valid Anagram

Problem:
Given two strings s and t, return True if t is an
anagram of s, and False otherwise.

An anagram is a word or phrase formed by rearranging
the letters of another word or phrase.

Examples:

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Approach:
Use two hash maps to count the frequency of each
character in both strings. Compare the two dictionaries.
If they are equal, the strings are anagrams.

Time Complexity: O(n + m)
Space Complexity: O(1), since there are only
26 possible lowercase English letters.

LeetCode:
https://leetcode.com/problems/valid-anagram/
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = {}
        n = {}

        for ch in s:
            if ch not in m:
                m[ch] = 1
            else:
                m[ch] += 1

        for ch in t:
            if ch not in n:
                n[ch] = 1
            else:
                n[ch] += 1

        if m == n:
            return True
        return False
