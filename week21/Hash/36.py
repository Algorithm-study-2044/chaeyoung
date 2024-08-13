class Solution:
    def isValidSudoku(self, board):
        def isCross(x, y, num):
            for i in range(9):
                if (i != y and board[x][i] == num) or (i != x and board[i][y] == num):
                    return False
            return True

        def isBox(x, y, num):
            boxX = x - (x % 3)
            boxY = y - (y % 3)

            for i in range(3):
                for j in range(3):
                    if ((boxX + i != x) and (boxY + j != y)) and board[boxX + i][boxY + j] == num:
                        return False

            return True

        def isSudoku(x, y, num):
            return isCross(x, y, num) and isBox(x, y, num)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and (not isSudoku(i, j, board[i][j])):
                    return False

        return True