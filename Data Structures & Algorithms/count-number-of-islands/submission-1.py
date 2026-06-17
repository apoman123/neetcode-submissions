class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length, width = len(grid), len(grid[0])

        def is_one(i, j):
            if grid[i][j] == "1":
                return True
            else:
                return False

        def find_candidates(i, j):
            candidates = []
            if i - 1 >= 0:
                if is_one(i-1, j):
                    candidates.append([i-1, j])
            if i + 1 < length:
                if is_one(i+1, j):
                    candidates.append([i+1, j])
            if j - 1 >= 0:
                if is_one(i, j-1):
                    candidates.append([i, j-1])
            if j + 1 < width:
                if is_one(i, j+1):
                    candidates.append([i, j+1])
            return candidates

        def dfs(pos):
            i, j = pos[0], pos[1]
            grid[i][j] = "0"
            candidates = find_candidates(i, j)
            for candidate in candidates:
                dfs(candidate)

        count = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == "1":
                    count += 1
                    dfs([i, j])

        return count
            
