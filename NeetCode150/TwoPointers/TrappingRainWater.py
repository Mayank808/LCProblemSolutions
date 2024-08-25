class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach #2 
        # two ptr no extra space complexity
        # we want to find min of max left and max right height at each postion
        # hence only the lowest height in a given spot matters

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        ret = 0
        while left < right:
            if max_left > max_right: # right is bottleneck
                right -= 1
                max_right = max(max_right, height[right])
                ret += max_right - height[right]
            else: # left is bottleneck
                left += 1
                max_left = max(max_left, height[left])
                ret += max_left - height[left]
        
        return ret

        # # Approach #1 
        # # find max prefix and max suffix arrays
        # ret = 0
        # max_left = [0] * len(height)
        # max_right = [0] * len(height)

        # for x in range(1, len(height)):
        #     max_left[x] = max(max_left[x - 1], height[x - 1])
        
        # for x in range(len(height) - 2, -1, -1):
        #     max_right[x] = max(max_right[x + 1], height[x + 1])
        
        # for i, h in enumerate(height):
        #     min_height = min(max_left[i], max_right[i])
        #     if min_height > h:
        #         ret += min_height - h

        # return ret
            
