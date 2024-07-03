class Solution:
    # [1 2 3 4 5] l < r
    # [3 4 5 1 2]
    # [4 5 1 2 3]
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1 
        cur_min = float('inf')
        while left <= right:
            if nums[left] < nums[right]:
                cur_min = min(cur_min, nums[left])
                break
            mid = (right - left) // 2 + left

            cur_min = min(cur_min, nums[mid])

            # normal b search
            if nums[left] <= nums[mid]:
                left = mid + 1 
            else:
                right = mid - 1

        return cur_min


