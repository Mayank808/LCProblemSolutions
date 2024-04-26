class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1 
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

        # Solution 2: One liner
        # return len(set(nums)) != len(nums)
