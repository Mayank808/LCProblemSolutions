class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # rephrasing problem 
        # goal is to find how many numbers are larger than a number at position x
        # we want to maximize the above problem statement
        # we can try to establish this from right to left
        # issue solution is worst case o(n^2)
        res = 1
        dp = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            j = i + 1
            dp[i] = 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j += 1

        # TODO: understand optimal binary search solution.
        
        return max(dp)
