class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        res = 0

        for price in prices:
            res = max(price - cur_min, res)
            cur_min = min(cur_min, price)

        return res

        # l, r = 0, 0
        # res = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         res = max(res, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1 

        # return res
