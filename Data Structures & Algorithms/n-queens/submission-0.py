class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = set()
        diags = set()
        anti_diags = set()

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols:
                    continue
                if row-col in diags:
                    continue
                if row+col in anti_diags:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                diags.add(row-col)
                anti_diags.add(row+col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diags.remove(row-col)
                anti_diags.remove(row+col)
        backtrack(0)
        return res