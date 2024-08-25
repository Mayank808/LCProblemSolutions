class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if not (0 <= row < rows):
                return 0
            
            if not (0 <= col < cols):
                return 0
            
            if not grid[row][col]:
                return 0
            
            grid[row][col] = 0

            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    ret = max(ret, dfs(row, col))
        

        return ret
