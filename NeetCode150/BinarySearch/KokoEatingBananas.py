class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force is to start at 1 -> inf to find k

        # Instead of incrementing k by 1 we can use a bsearch approach
        
        left = 1
        right = max(piles)
        minK = float('inf')
        while left <= right:
            mid = (right - left) // 2 + left 
            # print(f'left {left} right {right} Mid: {mid}')
            # mid will be out assumed k that we test with
            cur_hours = 0
            for bananas in piles:
                num_hours = math.ceil(bananas / mid)
                # print(f'Bananas {bananas}, num_hours: {num_hours}, cur_hours = {num_hours + cur_hours}')

                cur_hours += num_hours

                if cur_hours > h:
                    break
            
            if cur_hours > h:
                left = mid + 1
            else:
                right = mid - 1
                minK = min(mid, minK)


        return minK
