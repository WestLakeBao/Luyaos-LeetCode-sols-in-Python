# Given a string s, return the longest palindromic substring in s.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        def getLongestPalindrome(s, left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        for i in range(len(s)):
            temp1 = getLongestPalindrome(s, i, i)
            if len(temp1) > len(result):
                result = temp1
            temp2 = getLongestPalindrome(s, i, i + 1)
            if len(temp2) > len(result):
                result = temp2
        return result