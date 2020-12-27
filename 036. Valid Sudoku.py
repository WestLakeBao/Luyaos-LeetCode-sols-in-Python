# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# time: O()
# space: O()

class Solution(object):
    def isValidSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                x = i // 3
                y = j // 3
                num = board[i][j]
                if num in row[i] or num in col[j] or num in sub[x][y]:
                    return False
                else:
                    row[i].add(num)
                    col[j].add(num)
                    sub[x][y].add(num)
        return True

if __name__ == '__main__':
    print(Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))  # True
    print(Solution().isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))  # False