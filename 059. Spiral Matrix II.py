# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        result = [[0 for _ in range(n)] for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        num = 1
        while left <= right and up <= down:
            for i in range(left, right + 1):
                result[up][i] = num
                num += 1
            up += 1
            for i in range(up, down + 1):
                result[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                result[down][i] = num
                num += 1
            down -= 1
            for i in range(down, up - 1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result

print(Solution().generateMatrix(3)) # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]