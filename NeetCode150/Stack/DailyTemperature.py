class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        seen = []
        for i, temp in enumerate(temperatures):
            while seen and seen[-1][0] < temp:
                (_, index) = seen.pop()
                res[index] = i - index 
            seen.append((temp, i))

        return res
