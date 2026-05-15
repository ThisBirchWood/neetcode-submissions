class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_cols = {i: set() for i in range(9)}
        seen_subs = {i: set() for i in range(9)}
        for row in range(len(board)):
            seen_row = set()
            row_data = board[row]
            for col in range(len(row_data)):
                cell = row_data[col]

                if cell == ".":
                    continue
                
                if cell in seen_row:
                    return False
                seen_row.add(cell)

                if cell in seen_cols[col]:
                    return False
                seen_cols[col].add(cell)

                box_x = row // 3
                box_y = col // 3
                box = (box_x + (box_y * 3))
                if cell in seen_subs[box]:
                    return False
                seen_subs[box].add(cell)
                

        return True

            