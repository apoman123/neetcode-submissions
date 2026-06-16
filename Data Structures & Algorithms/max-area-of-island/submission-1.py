class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        columns = len(grid[0])
        max_area = 0
        global area 
    
        def dfs(i, j):
            global area
            stack = [[i, j]]
            while stack:
                new_i, new_j = stack.pop(0)
                area += 1
                grid[new_i][new_j] = 0
                for x, y in directions:
                    if new_i+x in range(rows) and new_j+y in range(columns):
                        if grid[new_i+x][new_j+y] == 1 and not [new_i+x, new_j+y] in stack:
                            stack.append([new_i+x, new_j+y])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    if area > max_area:
                        max_area = area
        
        return  max_area
