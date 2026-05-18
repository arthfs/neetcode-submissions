class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        columns = []
        rows = []
        squares = []
        for i in range(9):
            squares.append([])

        for i in range(m):
            columns.append([])
        
        for i in range(n):
            rows.append([])

        for i in range(n):
            for j in range(m):
                if board[i] [j] !='.':
                    if board[i][j] in rows[i]:
                        return False

                    if board[i] [j] in columns[j]:
                        return False

                    squareIndex = (i//3) * 3 + (j//3)
                    if squares[squareIndex].count(board[i][j]) != 0:
                        return False

                    squares[squareIndex].append(board[i][j])
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
        return True