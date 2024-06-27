class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for x in strs:
            s = ''.join(sorted(x))
            if s in groups:
                groups[s].append(x)
                continue
            groups[s] = [x]
        
        return groups.values()
