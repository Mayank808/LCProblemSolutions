from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums.sort()
        # print(nums)
        counts = Counter(nums)
        # print(counts)
        
        for num in nums:
            if not counts[num]:
                continue
            
            for x in range(num, num + k):
                if x not in counts:
                    return False
                
                counts[x] -= 1

        # while counts:
            
        #     min_val = next(iter(counts))
        #     # print(min_val, counts)
        #     for x in range(min_val, min_val + k):
        #         if x not in counts:
        #             return False
                
        #         counts[x] -= 1

        #         if not counts[x]:
        #             counts.pop(x)
        
        return True
