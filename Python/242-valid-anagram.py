
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
