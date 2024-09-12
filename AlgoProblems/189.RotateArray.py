class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        start = 0

        while start < len(nums) and count < len(nums):
            cur, prev = start, nums[start]
            while True:
                next_i = (cur + k) % len(nums)
                prev, nums[next_i] = nums[next_i], prev
                count += 1
                cur = next_i

                if cur == start:
                    break
            start += 1


        # def reverse(start, end):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1
        
        # n = k % len(nums)
        # reverse(0, len(nums) - 1)
        # reverse(0, n - 1)
        # reverse(n, len(nums) - 1)

        
