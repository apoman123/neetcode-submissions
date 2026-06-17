class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            numbers = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in numbers:
                    return False
                elif board[i][j] != "." and not board[i][j] in numbers:
                    numbers.add(board[i][j])
        

        # check columns
        for j in range(9):
            numbers = set()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in numbers:
                    return False
                elif board[i][j] != "." and not board[i][j] in numbers:
                    numbers.add(board[i][j])

        grids = [[0,1,2], [3,4,5], [6,7,8]]
        for row_grid in grids:
            for column_grid in grids:
                numbers = set()
                for i in row_grid:
                    for j in column_grid:
                        if board[i][j] != "." and board[i][j] in numbers:
                            return False
                        elif board[i][j] != "." and not board[i][j] in numbers:
                            numbers.add(board[i][j])
        return True

