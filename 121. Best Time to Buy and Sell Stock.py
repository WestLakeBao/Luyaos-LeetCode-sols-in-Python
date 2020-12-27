# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        sellout = prices[-1]
        profit = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > sellout:
                sellout = prices[i]
            profit = max(profit, sellout - prices[i])
        return profit
    

if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0