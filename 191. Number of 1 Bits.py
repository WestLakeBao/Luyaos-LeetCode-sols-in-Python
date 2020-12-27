# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

class Solution(object):
    def hammingWeight(self, n):
        result = 0
        while n:
            result += n & 1
            n /= 2
        return result