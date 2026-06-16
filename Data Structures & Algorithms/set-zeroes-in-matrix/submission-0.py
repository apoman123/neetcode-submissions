class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zero_locs = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_locs.append([i, j])
                
        for loc in zero_locs:
            for i in range(len(matrix)):
                matrix[i][loc[1]] = 0
            for j in range(len(matrix[0])):
                matrix[loc[0]][j] = 0