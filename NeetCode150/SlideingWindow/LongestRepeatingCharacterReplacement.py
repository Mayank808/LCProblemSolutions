class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        seen = {}
        res = 0
        left = 0

        # res is maximized when max_freq is maxed hence we dont need to recalculate max_freq
        for right, c in enumerate(s):
            seen[c] = 1 + seen.get(c, 0) # if c not in dict return 0
            max_freq = max(max_freq, seen[c])

            while (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

