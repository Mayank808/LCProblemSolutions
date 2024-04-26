from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # return Counter(s) == Counter(t)

        counts = Counter(s)

        for x in t:
            if not counts[x]: return False
            counts[x] -= 1
        
        return True
