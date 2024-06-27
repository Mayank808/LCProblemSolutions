from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        counts = Counter(nums)
        
        for num, count in counts.items():
            if count == 1:
                return -1

            # could also use ceiling or a simpler approach using division by 3 and add 1 to result if remainder is > 0
            # went with this as it is a verbose solution making it easier to understand and read for me.
            greedy_3 = greedy_2 = 0
            if not count % 3:
                greedy_3 = count // 3
            elif count % 3 == 1:
                greedy_2 = 2
                if count - 4 > 0:
                    greedy_3 = (count - 4) // 3 
            else: # count % 3 == 2
                greedy_3 = count // 3
                greedy_2 = (count % 3) // 2
            
            res += greedy_3 + greedy_2


        return res
