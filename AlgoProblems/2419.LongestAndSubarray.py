class Solution:
    def longestSubarray(self, nums: List[int]) -> int: 
        # and with a larger or smaller number then the max results in a smaller number
        # so its just a question about checking how many max values are next to each other 
          
        max_val, cur, res = max(nums), 0, 0
        for val in nums:
            if val == max_val:
                cur += 1
            else:
                res = max(cur, res)
                cur = 0
            
        return max(cur, res)
