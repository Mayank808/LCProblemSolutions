# Have to sort and then this problem devolves to 2SumII 
# Have to remember to deal with dupes with both main loop and when s == target case occurs. 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        x = 0
        nums.sort()

        # Solution
        while x < len(nums) - 2:
            target = 0 - nums[x]
            left = x + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([nums[x], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s > target:
                    right -= 1
                else:
                    left += 1
            
            x += 1

            while x < len(nums) and nums[x] == nums[x - 1]:
                x += 1
        
        return res

        # # Slightly cleaner Pythonic Implementation 
        # for i, val in enumerate(nums):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     target = 0 - val
        #     left = i + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         s = nums[left] + nums[right]

        #         if s == target:
        #             res.append([val, nums[left], nums[right]])
        #             left += 1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        #         elif s > target:
        #             right -= 1
        #         else:
        #             left += 1
