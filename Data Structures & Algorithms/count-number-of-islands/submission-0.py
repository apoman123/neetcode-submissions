class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        rows, columns = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0

        def dfs(grid, row, column):
            stack = [(row, column)]
            while stack:
                current_row, current_column = stack.pop()
                visit.add((current_row, current_column))
                for r, c in directions:
                    new_row, new_column = current_row + r, current_column + c
                    if (new_row in range(rows) and
                        new_column in range(columns) and
                        grid[new_row][new_column] == "1" and
                        (new_row, new_column) not in visit
                    ):
                        stack.append((new_row, new_column))


        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(grid, i, j)
                    islands += 1
        
        return islands