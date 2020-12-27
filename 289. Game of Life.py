# According to the Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
# (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
# The next state is created by applying the above rules simultaneously to every cell in the current state,
# where births and deaths occur simultaneously.

class Solution(object):
    def gameOfLife(self, board):
        row_len = len(board)
        col_len = len(board[0])
        count_live = [[0] * col_len for _ in range(row_len)]
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == 1:
                    for k in range(max(0, row-1), min(row+2, row_len)):
                        for l in range(max(0, col-1), min(col+2, col_len)):
                            count_live[k][l] += 1
                    count_live[row][col] -= 1
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == 1:
                    if count_live[row][col] < 2 or count_live[row][col] > 3:
                        board[row][col] = 0
                elif board[row][col] == 0:
                    if count_live[row][col] == 3:
                        board[row][col] = 1
        return board