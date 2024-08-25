class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # ideas
        # 1. can either bloom out of chest and fill in the lands with respectives values
        # 2. or can dfs and backtrack from each land piece and fill everything filled along the way

        # Approach one seems better as I assum there will be less 


        # overwrite grid can also create new
        rows, cols = len(grid), len(grid[0])

        # dfs will travers from a chest and bloom out to all nearest 
        # can also use bfs shortest path approach both about the same
        def dfs(row, col, dist):
            if not (0 <= row < rows):
                return
            
            if not (0 <= col < cols):
                return
            
            if grid[row][col] == -1 or (grid[row][col] == 0 and dist):
                return
            
            if grid[row][col] < dist:
                return
            
            grid[row][col] = dist

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + x, col + y, dist + 1)

            

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: # found a chest
                    dfs(row, col, 0)
