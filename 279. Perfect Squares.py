# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

class Solution(object):
    def numSquares(self, n):
        dp = [n] * (n + 1)
        for i in range(int(n ** 0.5) + 1):
            dp[i * i] = 1
        for i in range(1, n + 1):
            for j in range(int(i ** 0.5) + 1):
                if i + j * j <= n:
                    dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
        return dp[n]