# Given a column title as appear in an Excel sheet, return its corresponding column number.

class Solution(object):
    def titleToNumber(self, s):
        result = 0
        for i in range(len(s)):
            result = (ord(s[i]) - ord('A') + 1) + 26 * result
        return result