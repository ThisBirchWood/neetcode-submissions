import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        sub = {}

        for i in range(9):
            rows[i] = {}
            columns[i] = {}
            sub[i] = {}

        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                current_num = board[i][j]

                if current_num == ".":
                    continue

                current_num = int(current_num)

                if current_num in rows[i]:
                    return False
                rows[i][current_num] = True

                if current_num in columns[j]:
                    return False
                columns[j][current_num] = True

                subbox = ((i // 3)*3) + (j // 3)

                if current_num in sub[subbox]:
                    return False
                sub[subbox][current_num] = True
        return True