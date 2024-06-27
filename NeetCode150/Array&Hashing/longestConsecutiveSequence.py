# Trick: check if the number can be the first number in a sequence ie n - 1 not in set. Worst case O(n + n) => O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Optimal Solution: O(n)
        ns = set(nums)
        res = 0

        for num in ns:
            if num - 1 in ns:
                continue
            
            length = 1
            val = num
            while val + 1 in ns:
                length += 1
                val += 1
            
            res = max(length, res)

        return res

        # # Solution #3: Union Find esq approach: O(n)
        # ns = set(nums) 
        # res = 0
        # seen = {}

        # for num in ns:
        #     if num in seen: continue

        #     cur_res = 1
        #     val = num
        #     while val - 1 in ns: # at max will do O(n) iterations
        #         val -= 1
        #         if val in seen:
        #             cur_res += seen[val]
        #             break
        #         cur_res += 1
        #         seen[val] = cur_res

            
        #     res = max(res, cur_res)
        #     seen[num] = cur_res
        
        # return res

        # # Solution #2: O(nlogn) 

        # # Solution #1: O(n^2)
        # seen = set(nums) # O(n)

        # res = 0
        # for num in nums:
        #     cur_res = 1
        #     val = num 
        #     while val - 1 in seen: # worst case O(n)
        #         cur_res += 1
        #         val -= 1
                
        #     res = max(res, cur_res)
        
        # return res
                
            
