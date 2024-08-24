class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        def dfs(index, csum, combo):
            if csum > target:
                return
            
            if csum == target:
                ret.append(combo[:])
                return 
            
            if index >= len(candidates):
                return
            
            # include index
            combo.append(candidates[index])
            dfs(index, csum + candidates[index], combo)
            combo.pop()
            
            # dont include cur num
            dfs(index + 1, csum, combo)
        
        dfs(0, 0, [])
        return ret
