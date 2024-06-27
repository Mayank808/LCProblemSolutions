class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        # two pointer
        # sort both then linear two pointer compare arrays
        # o(min(n,m) + logn + logm)
        s.sort()
        g.sort()
        S, G = 0, 0
        while S < len(s) and G < len(g):
            if s[S] >= g[G]:
                res += 1
                G += 1
            S += 1
            

        # bsearch solution
        # loop through one array and binary search for value >= curr in second array
        # o(nlogm)
        '''
        s.sort()
        for child in g:
            if not len(s):
                break

            left = 0
            right = len(s) - 1
            while left <= right:
                mid = (left + right) // 2

                if s[mid] == child:
                    res += 1
                    s.pop(mid)
                    break
                elif s[mid] < child:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if left < len(s) and s[left] >= child:
                    res += 1
                    s.pop(left)
        '''
        
        return res

            
