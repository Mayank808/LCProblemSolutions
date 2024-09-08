class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        ps1, ps2 = 0, 0
        # print(slots1, slots2)
        while ps1 < len(slots1) and ps2 < len(slots2):
            max_x = max(slots1[ps1][0], slots2[ps2][0])
            min_y = min(slots1[ps1][1], slots2[ps2][1])

            # print(slots1[ps1], slots2[ps2], max_x, min_y, min_y - max_x)
            if max_x <= min_y and min_y - max_x >= duration:
                return [max_x, max_x + duration]
            elif slots1[ps1][1] < slots2[ps2][1]:
                ps1 += 1
            else:
                ps2 += 1

        return []
