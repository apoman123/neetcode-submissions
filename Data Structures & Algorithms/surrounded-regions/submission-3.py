class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, columns = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, new_mark, board):
            board[i][j] = new_mark
            for x, y in directions:
                if i+x in range(rows) and j+y in range(columns):
                    if board[i+x][j+y] == "O":
                        dfs(i+x, j+y, new_mark, board)

                 

        def change_to_mark(mark, new_mark, board):
            for column in range(columns):
                if board[0][column] == mark:
                    dfs(0,column, new_mark, board)
                if board[rows-1][column] == mark:
                    dfs(rows-1,column, new_mark, board)

            for row in range(rows):
                if board[row][0] == mark:
                    dfs(row, 0, new_mark, board)
                if board[row][columns - 1] == mark:
                    dfs(row, columns-1, new_mark, board)
        
        change_to_mark("O", "T", board)

        print(board)

        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "O":
                    board[row][column] = "X"
        
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "T":
                    board[row][column] = "O"
        
    
        
