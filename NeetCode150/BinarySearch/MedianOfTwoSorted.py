class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        n = len(a) + len(b)
        half = n // 2

        # assure that smallest array is always the one we run b search on
        if len(nums2) < len(nums1):
            a, b = b, a

        left, right = 0, len(a) - 1

        # will always find a solution with this
        while True:
            # mid will repersent the slice of our A array that is on the left of the median
            mid = (right - left) // 2 + left

            # repersents the slice of B that is on the left side of median
            leftover = half - mid - 2

            # index errors can occur as its possible for none of a or b to be on left side
            leftA = a[mid] if mid >= 0 else float("-inf")
            rightA = a[mid + 1] if (mid + 1) < len(a) else float("inf")
            leftB = b[leftover] if leftover >= 0 else float("-inf")
            rightB = b[leftover + 1] if (leftover + 1) < len(b) else float("inf")

            # valid slice occurs if left part of the slice on both arrays is smaller then the right on the other
            if leftB <= rightA and leftA <= rightB:
                # even cause 
                if n % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                
                # odd case
                return min(rightA, rightB)

            # current B has smaller values then A that should be on the left side of median
            # shrink slice in array A
            elif leftA > rightB:
                right = mid - 1

            # current B slice has values greater then median should increase 
            # left slice to get smaller values
            else:
                left = mid + 1



            
