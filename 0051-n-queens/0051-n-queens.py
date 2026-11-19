class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        pos_diag = set()  # Tracks (row + col) diagonals
        neg_diag = set()  # Tracks (row - col) diagonals

        def backtrack(row: int):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                # Place the queen
                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                # Move to the next row
                backtrack(row + 1)

                # Remove the queen (backtrack)
                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)
        return res
