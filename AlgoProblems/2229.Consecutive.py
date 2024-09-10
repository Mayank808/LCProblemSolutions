class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        vals = set(nums)
        
        # must exist n unique values
        if len(vals) != len(nums):
            return False

        # those n unique values must be in the consecutive range
        min_v = min(vals)
        max_v = max(vals)

        # print(min_v, max_v)
        return min_v + len(nums) - 1 == max_v

        # nums.sort()
        
        # for x in range(1, len(nums)):
        #     if nums[x - 1] + 1 != nums[x]:
        #         return False
        
        # return True
