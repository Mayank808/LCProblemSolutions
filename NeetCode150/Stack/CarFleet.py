class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip together position and speed into array of tuples
        # sort by position and iterate right through left comparing on time to reach end

        # loop through zipped array
        startSpeed = [(p, s) for p, s in zip(position, speed)]
        startSpeed = sorted(startSpeed, reverse=True)
        ret = []
        for pos, spe in startSpeed:
            timeToEnd = (target - pos) / spe
            if not ret or ret[-1] < timeToEnd:
                ret.append(timeToEnd)
        
        return len(ret)

        
