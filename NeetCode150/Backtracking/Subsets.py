class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack approach
        # each position recurse with either including the index or not

        ## Apprach #2
        # ret = []

        # def dfs(index, subset):
        #     ret.append(subset[:])

        #     if index >= len(nums):
        #         return
            
        #     for x in range(index, len(nums)):
        #         subset.append(nums[x])
        #         dfs(x + 1, subset)
        #         subset.pop()
            
        
        # dfs(0, [])
        # return ret

        # Approach 1
        ret = []
        def backtrack(index, arr):
            if index >= len(nums):
                ret.append(arr[:])
                return

            # dont add value to arr 
            arr.append(nums[index])
            backtrack(index + 1, arr)
            
            arr.pop()
            backtrack(index + 1, arr)

        
        backtrack(0, [])
        return ret
