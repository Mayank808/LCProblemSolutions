class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        val = 0
        valid = set(allowed)
        for word in words:
            if set(word) <= valid:
                val += 1
        
        return val
