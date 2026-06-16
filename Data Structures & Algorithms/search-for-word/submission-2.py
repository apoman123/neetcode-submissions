class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        rows = len(board)
        columns = len(board[0])
        global prev_idx, has_word
        prev_idx = []
        has_word = False
        def searching(i, j):
            global prev_idx, has_word
            # print("".join([board[i][j] for i, j in prev_idx]))
            # print(len(prev_idx))
            prev_idx.append([i, j])
            if len(prev_idx) == len(word):
                if "".join([board[i][j] for i, j in prev_idx]) == word:
                    has_word = True
            else:
                for x, y in directions:
                    if i+x in range(rows) and j+y in range(columns) and not [i+x, j+y] in prev_idx:
                        searching(i+x, j+y)

            prev_idx.pop()

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    searching(i, j)
        
        return has_word
                    


         