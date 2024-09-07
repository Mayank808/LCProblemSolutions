from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def isSqrt2(num):
            return num != 0 and num & (num - 1) == 0
        
        mod = 10 ** 9 + 7
        counts = Counter(deliciousness)
        vals = 0
        valid_powers = [1 << n for n in range(22)]
        for num, count in counts.items():

            for p2 in valid_powers:
                if p2 - num >= 0 and p2 - num in counts:
                    vals += count * (counts[p2 - num] - 1 if p2 - num == num else counts[p2 - num])




        # find all unique pairs in array such that their sum is equal to a power of 2
        # navie approach
        # pairs = []
        # vals = 0

        # for left in range(len(deliciousness)):
        #     for right in range(left + 1, len(deliciousness)):
        #         if isSqrt2(deliciousness[left] + deliciousness[right]):
        #             # pairs.append((deliciousness[left], deliciousness[right]))
        #             vals += 1
        
        return (vals // 2) % mod
