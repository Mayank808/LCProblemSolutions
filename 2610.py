class Solution:
    # using a dictionary can determine count
    # if number exists in dictionary means its a duplicate hence add to poistion count
    # if not in dicitonary then can add into positon 0
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        res = [[]]
        for x in nums:
            if x not in seen:
                seen[x] = 1
                res[0].append(x)
                continue

            if len(res) < seen[x] + 1:
                res.append([])

            res[seen[x]].append(x)
            seen[x] += 1
        
        return res
