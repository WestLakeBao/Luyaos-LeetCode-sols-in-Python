# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        row_len = len(matrix)
        col_len = len(matrix[0])
        up, down, left, right = 0, row_len-1, 0, col_len-1
        result = []
        while left < right and up < down:
            result.extend(matrix[up][i] for i in range(left, right))
            result.extend(matrix[j][right] for j in range(up, down))
            result.extend(matrix[down][i] for i in range(right, left, -1))
            result.extend(matrix[j][left] for j in range(down, up, -1))
            up, down, left, right = up+1, down-1, left+1, right-1
        if up == down:
            result.extend(matrix[up][i] for i in range(left, right+1))
        elif left == right:
            result.extend(matrix[j][left] for j in range(up, down+1))
        return result

print(Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(Solution().spiralOrder([])) # []