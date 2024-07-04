# Design concepts
    # Approach 1: { key : [(timestamp, value)]}: issue [(timestamp, value)] needs to be sorted otherwise linear search
    # Approach 2: { key : { timestamp : value }}: better but need a way to find max timestamp_prev

    # Approach 2 is better as we can search for max timestamp_prev using bsearch left = 1 right = timestamp
    # and nested dictionaries allows for easy O(1) lookup

    # questions
    # can there be multiple values with same timestamp under one key?

# Issues with Leetcode description
# WHY IS THIS IN THE CONSTRAINTS AND NOT THE MAIN PROBLEM!!!!!
# "All the timestamps timestamp of set are strictly increasing."

# Because of above we can use approach 1 and run bsearch

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        # self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(f'Called set with key {key} value {value} timestamp {timestamp}')
        
        self.timeMap[key].append((value, timestamp))

        # # can use default dict with array and simplfy logic
        # if key in self.timeMap:
        #     self.timeMap[key].append((value, timestamp))
        # else:
        #     self.timeMap[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        left = 0 
        right = len(self.timeMap[key]) - 1

        cur_val = ""
        while left <= right:
            mid = (right - left) // 2 + left
            (val, time) = self.timeMap[key][mid]
            if time == timestamp:
                return val
            elif time < timestamp:
                left = mid + 1
                cur_val = val
            else:
                right = mid - 1
            # print(left, right, mid, time, timestamp, self.timeMap[key])

        return cur_val

# # Approach #2: better if assumption wasent there of increasing inserts
# class TimeMap:

#     def __init__(self):
#         self.timeMap = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         # print(f'Called set with key {key} value {value} timestamp {timestamp}')

#         if key in self.timeMap:
#             self.timeMap[key][timestamp] = value
#         else:
#             self.timeMap[key] = {timestamp : value}
        
#     def get(self, key: str, timestamp: int) -> str:
#         # O(n) approach tle. approach if assumption didnt exist of increasing inserts 
#         # check if timestamp in self.timeMap[key]
#         if key not in self.timeMap:
#             return ""
        
#         if timestamp in self.timeMap[key]:
#             return self.timeMap[key][timestamp]

#         res = ""
#         cur_max_t = 0
#         for t, value in self.timeMap[key].items():
#             if t <= timestamp and cur_max_t < t:
#                 res = value
#                 cur_max_t = t
                
#         return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
