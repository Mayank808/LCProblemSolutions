# import heapq 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimal Soluton: O(n)
        counts = Counter(nums) # O(n)
        buckets = [[] for _ in range(len(nums))]

        for num, count in counts.items():
            buckets[count - 1].append(num)
            
        res = []
        for x in range(len(nums) - 1, -1, -1):
            for num in buckets[x]:
                res.append(num)
                if len(res) == k:
                    return res

        # # Solution #1: O(klog(n))
        # counts = Counter(nums) # O(n)
        # heap = []
        # for key, count in counts.items(): # O(n)
        #     heap.append((-count, key))
        # heapq.heapify(heap) # O(n)
        # return [heapq.heappop(heap)[1] for _ in range(k)] # O(klog(n))

        # # Solution #2: O(nlogn)
        # counts = Counter(nums) # O(n)
        # tups = [(count, num) for num, count in counts.items()] # O(n)
        # tups.sort(reverse = True, key = lambda x: x[0]) # O(nlogn)
        # return [tups[x][1] for x in range(k)] # O(k)
