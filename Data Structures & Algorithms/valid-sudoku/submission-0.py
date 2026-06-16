class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        # check columns
        # check boxes

        for row in range(9):
            numbers = [str(idx) for idx in range(1, 10)]
            for column in range(9):
                if board[row][column] != "." and board[row][column] in numbers:
                    numbers.remove(board[row][column])
                elif board[row][column] != "." and not board[row][column] in numbers:
                    return False

        for column in range(9):
            numbers = [str(idx) for idx in range(1, 10)]
            for row in range(9):
                if board[row][column] != "." and board[row][column] in numbers:
                    numbers.remove(board[row][column])
                elif board[row][column] != "." and not board[row][column] in numbers:
                    return False

        boxes = [[0,1,2], [3,4,5], [6,7,8]]
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                rows, columns = boxes[i], boxes[j]
                numbers = [str(idx) for idx in range(1, 10)]
                for row in rows:
                    for column in columns:
                        if board[row][column] != "." and board[row][column] in numbers:
                            numbers.remove(board[row][column])
                        elif board[row][column] != "." and not board[row][column] in numbers:
                            return False

        return True
                        
        

        
                