class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = [int(time[0:2]) * 60 + int(time[3:]) for time in timePoints]
        
        mins.sort()

        dists = min([mins[x] - mins[x - 1] for x in range(1, len(mins))])
        
        return min(dists, mins[0] + 60 * 24 - mins[-1])
        
