class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Bitwise operators
        res = 0 
        while start or goal:
            if (start & 1) != goal & 1:
                res += 1
            start = start >> 1
            goal = goal >> 1
            
        return res

        # # Xor approach
        # xor = start ^ goal
        # res = 0
        # while xor:
        #     res += xor & 1
        #     xor = xor >> 1

        # return res


        # # Bin matching approach lol: bad
        # res = 0
        # if start == goal:
        #     return res
        
        # s, g = bin(start), bin(goal)        
        # s1, g1 = len(s) - 1, len(g) - 1
    
        # while s1 > 1 and g1 > 1:
        #     if s[s1] != g[g1]:
        #         res += 1
        #     s1 -= 1
        #     g1 -= 1
        
        # while s1 > 1:
        #     if s[s1] == "1":
        #         res += 1
        #     s1 -= 1
        
        # while g1 > 1:
        #     if g[g1] == "1":
        #         res += 1
        #     g1 -= 1
            
        
        # return res 
            


