class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for x in range(1, n):
            res[x] *= nums[x - 1] * prefix
            prefix *= nums[x - 1]
        
        suffix = nums[-1]
        for x in range(n - 2, -1, -1):
            res[x] *= suffix
            suffix *= nums[x]

        return res
