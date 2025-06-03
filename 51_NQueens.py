class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(solutions: List[List[str]], board: List[List[str]],
            column: List[bool], ldiag: List[bool], rdiag: List[bool], row: int):
            n = len(board)
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            for i in range(n):
                if column[i] or ldiag[n - row + i - 1] or rdiag[row + i]:
                    continue

                board[row][i] = "Q"
                column[i] = ldiag[n - row + i - 1] = rdiag[row + i] = True
                backtracking(solutions, board, column, ldiag, rdiag, row + 1)

                board[row][i] = "."
                column[i] = ldiag[n - row + i - 1] = rdiag[row + i] = False

        solutions = []
        board = [["." for _ in range(n)] for _ in range(n)]
        column = [False] * n

        ldiag = [False] * (2 * n - 1)
        rdiag = [False] * (2 * n - 1)
        
        backtracking(solutions, board, column, ldiag, rdiag, 0)
        return solutions
