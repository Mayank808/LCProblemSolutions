from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # ends of arrays will have count of 1
        edges = defaultdict(list)

        for left, right in adjacentPairs:
            edges[left].append(right)
            edges[right].append(left)


        start = []
        arr = []
        for key, val in edges.items():
            if len(val) == 1:
                start.append(key)
                break
        
        seen = set()
        while start:
            val = start.pop()
            arr.append(val)
            seen.add(val)

            for child in edges[val]:
                if child in seen:
                    continue
                start.append(child)
        
        return arr
                
