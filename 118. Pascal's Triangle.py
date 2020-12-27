# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution(object):
    def generate(self, numRows):
        triangle = []
        if numRows == 0:
            return triangle
        triangle.append([1])

        for i in range(2, numRows + 1):
            newRow = [0 for _ in range(i)]
            newRow[0] = 1
            newRow[-1] = 1

            for j in range(1, i - 1):
                newRow[j] = triangle[i - 2][j - 1] + triangle[i - 2][j]
            triangle.append(newRow)
        return triangle

if __name__ == '__main__':
    print(Solution().generate(numRows=5))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]