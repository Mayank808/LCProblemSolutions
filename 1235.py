class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for p, start, end in zip(profit, startTime, endTime):
            jobs.append((start, end, p))
        
        # need to do a similar bsearch dp top-down approach to yesterdays problem 
        # this can also be done using a dfs bsearch caching recursive approach
        # for index, (start, end, profit) in enumerate(jobs):
        #     dp[index] = profit
        #     left = 0
        #     right = index - 1

        dp = [0] * (len(jobs) + 1)
        jobs.sort()
        for i in range(len(jobs) - 1, -1, -1):
            start, end, profit = jobs[i]

            # conduct a binary search to find the first interval that has a start time <= end time
            left = bisect.bisect_left(jobs, (end, float(-inf), float(-inf)))
            # above one liner does same as below 
            # left = i + 1
            # right = len(jobs) - 1
            # while left <= right:
            #     mid = (right + left) // 2
            #     s, e, p = jobs[mid]
            #     if end > s:
            #         left = mid + 1
            #     else: 
            #         right = mid - 1
            
            dp[i] = max(dp[i + 1], profit + dp[left])
        return dp[0]

        # dp approach
        # similar to problem 300, work down from latest start time down
        # o(n^2) worst case and tles on problem input
        '''
        dp = [0] * len(jobs)
        jobs.sort(reverse=True)
        for index, (start, end, profit) in enumerate(jobs):
            dp[index] = profit
            for j in range(index - 1, -1, -1):
                s, e, p = jobs[j]
                if end <= s:
                    dp[index] = max(dp[index], profit + dp[j])

        return max(dp)
        '''

        # naive approach
        # dfs recursive approach to exhaust all possible variations
        # o(2^n) will def tle
        # above could be further optamized if we cache but is still not great.

