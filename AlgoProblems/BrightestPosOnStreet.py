from collections import defaultdict
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = defaultdict(int)

        for pos, light_range in lights:
            events[pos - light_range] += 1
            events[pos + light_range + 1] -= 1

        
        maxSum, lsum = 0, 0
        maxPos = -1
        for pos, val in sorted(events.items()):
            lsum += val
            if lsum > maxSum:
                maxSum = lsum
                maxPos = pos

        return maxPos
