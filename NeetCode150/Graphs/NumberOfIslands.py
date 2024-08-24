class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        # if unable to mutate grid create a visited set of coords and check if we are in visited
        def dfs(row, col):
            if not (0 <= row < len(grid)):
                return
            
            if not (0 <= col < len(grid[0])):
                return
            
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1": # and not visited if cant mutate grid
                    ret += 1
                    dfs(row, col)
        

        return ret
