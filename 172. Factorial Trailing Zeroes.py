# Given an integer n, return the number of trailing zeroes in n!.

class Solution(object):
    def trailingZeroes(self, n):
        result = 0
        i = 5
        while i <= n:
            result += n // i
            i *= 5
        return result