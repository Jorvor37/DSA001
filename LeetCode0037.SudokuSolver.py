"""
Q: Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy regular rules
Initial thought on this solving technique was to verify that my currect cells is allow to put that number or not
1. Create checker function called is_valid
2. We run thorught and check only empty cells with this line if board[r][c] == ".":
3. Then we try everynumber by use created function above
4. Backtrack the cells that not filled with new information

with this back tracking method I reached Time Limit Exceeded, may be we try this attempt later
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num):
            #row
            for i in range(9):
                if board[row][i] == num:
                    return False
            #column
            for j in range(9):
                if board[j][col] == num:
                    return False
            #Grid
            before_row = (row // 3) * 3
            before_col = (col // 3) * 3
            for i in range(before_row, before_row + 3):
                for j in range(before_col, before_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(board, r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        backtrack()
        
