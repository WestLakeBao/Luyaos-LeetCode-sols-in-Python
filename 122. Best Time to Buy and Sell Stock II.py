# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0